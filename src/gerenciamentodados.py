from db.db_managment import DatabaseManager
from .obrafisica import ObraFisica
from .livro import Livro
from .periodico import Periodico

class GerenciamentoDados:
    @staticmethod
    def inserirObra(item: ObraFisica):
        db = DatabaseManager()
        db.connect()
        try:
            db.start_transaction()

            # Inserir na tabela ObraFisica
            obra_fisica_query = """
            INSERT INTO ObraFisica (id, titulo, paginas, data_publicacao, quantidade)
            VALUES (%s, %s, %s, %s, %s)
            """
            obra_fisica_id = item.id
            db.execute_query(obra_fisica_query, (obra_fisica_id, item.titulo, item.paginas, item.data_publicacao, item.quantidade))
            
            # Inserir na tabela Autor
            autor_query = """
            INSERT INTO Autor (nome, obra_fisica_id)
            VALUES (%s, %s)
            """
            for autor in item.autor:
                db.execute_query(autor_query, (autor, obra_fisica_id))

            # Inserir na tabela Livro ou Periodico dependendo do tipo da obra
            if isinstance(item, Livro):
                livro_query = """
                INSERT INTO Livro (ISBN, editora, genero)
                VALUES (%s, %s, %s)
                """
                db.execute_query(livro_query, (obra_fisica_id, item.editora, item.genero))
            elif isinstance(item, Periodico):
                periodico_query = """
                INSERT INTO Periodico (ISSN, editora, area_estudo, volume)
                VALUES (%s, %s, %s, %s)
                """
                db.execute_query(periodico_query, (obra_fisica_id, item.editora, item.area_estudo, item.volume))

            # Inserir na tabela Exemplar
            exemplar_query = """
            INSERT INTO Exemplar (numero, estado, obra_fisica_id)
            VALUES (%s, %s, %s)
            """
            for (numero, estado) in item.exemplar.items():
                db.execute_query(exemplar_query, (numero, estado, obra_fisica_id))

            # Comitar a transação se tudo deu certo
            db.commit()
            print("Obra inserida com sucesso")
        except Exception as e:
            # Reverter a transação em caso de erro
            db.rollback()
            print(f"Erro ao inserir obra: {e}")
        finally:
            db.disconnect()

    @staticmethod
    def pesquisarObraPorTitulo(string: str) -> list[ObraFisica]:
        db = DatabaseManager()
        db.connect()
        try:
            # Pesquisa por título na tabela ObraFisica
            result = db.search_by_parameter("ObraFisica", "titulo", string)

            if result:
                obras: list[ObraFisica] = []
                for row in result:
                    obra_id = row['id']
                    titulo = row['titulo']
                    paginas = row['paginas']
                    data_publicacao = row['data_publicacao']
                    quantidade = row['quantidade']

                    # Buscar os autores da obra
                    query_autores = "SELECT nome FROM Autor WHERE obra_fisica_id = %s"
                    autores_result = db.fetch_all(query_autores, (obra_id,))
                    autores = [autor['nome'] for autor in autores_result]

                    # Determinar o tipo da obra e buscar os detalhes específicos
                    query_livro = "SELECT * FROM Livro WHERE ISBN = %s"
                    livro_result = db.fetch_all(query_livro, (obra_id,))

                    if livro_result:
                        detalhes = Livro(livro_result[0]['editora'], livro_result[0]['ISBN'], livro_result[0]['genero'], titulo, autores, data_publicacao, paginas, quantidade)
                        obras.append(detalhes)
                    else:
                        query_periodico = "SELECT * FROM Periodico WHERE ISSN = %s"
                        periodico_result = db.fetch_all(query_periodico, (obra_id,))
                        if periodico_result:
                            detalhes = Periodico(periodico_result[0]['ISSN'], periodico_result[0]['editora'], periodico_result[0]['area_estudo'], periodico_result[0]['volume'])
                            obras.append(detalhes)

                return obras
            else:
                print("Nenhuma obra encontrada com o título fornecido")
                return []
        except Exception as e:
            print(f"Erro ao pesquisar obra: {e}")
            return []
        finally:
            db.disconnect()

# Exemplo de uso
teste = Livro('leia', '2589631458', 'terror', 'unico', ['jorge'], '2020-04-04', 50, 5) 
GerenciamentoDados.inserirObra(teste)
results = GerenciamentoDados.pesquisarObraPorTitulo('unico')
for obra in results:
    print(obra.retornar_atributos())
