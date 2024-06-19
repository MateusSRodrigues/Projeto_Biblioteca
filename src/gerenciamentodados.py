from db.db_managment import *
from .obrafisica import ObraFisica
from .livro import Livro
from .trabalhoacademico import TrabalhoAcademico
from .periodico import Periodico


class gerenciamentodados():
    def inserirObra(Item : ObraFisica):

        db = DatabaseManager()
        db.connect()
        try:
            db.start_transaction()

            # Inserir na tabela ObraFisica
            obra_fisica_query = """
            INSERT INTO ObraFisica (titulo, paginas, data_publicacao, quantidade)
            VALUES (%s, %s, %s, %s)
            """
            obra_fisica_id = db.execute_query(obra_fisica_query, (Item._titulo, Item._paginas, Item._data_publicacao, Item._quantidade))
            if obra_fisica_id is None:
                raise Exception("Failed to insert into ObraFisica")

            # Inserir na tabela Autor
            atributus = Item.retornar_atributos()
            autor_query = """
            INSERT INTO Autor (nome, obra_fisica_id)
            VALUES (%s, %s)
            """

            """
            autor_id = db.execute_query(autor_query, (Item._autor[0], obra_fisica_id))
            if autor_id is None:
                raise Exception("Failed to insert into Autor")
            """
            for autori in Item.autor:
                autor_id = db.execute_query(autor_query, (autori, obra_fisica_id))
                if autor_id is None:
                    raise Exception(f"Failed to insert author {autori} into Autor")
            
            # Inserir na tabela Livro
            livro_query = """
            INSERT INTO Livro (id, ISBN, editora, genero)
            VALUES (%s, %s, %s, %s)
            """
            livro_id = db.execute_query(livro_query, (obra_fisica_id, atributus[5],atributus[6],atributus[7]))
            if livro_id is None:
                raise Exception("Failed to insert into Livro")
            
            # Inserir na tabela Exemplar (para cada volume e estado)
            exemplar_query = """
            INSERT INTO Exemplar (numero, estado, obra_fisica_id)
            VALUES (%s, %s, %s)
            """
            for (volume, estado) in Item._exemplar.items():
                exemplar_id = db.execute_query(
                    exemplar_query, (volume, estado, obra_fisica_id)
                )
                if exemplar_id is None:
                    raise Exception("Failed to insert into Exemplar")

            # Comitar a transação se tudo deu certo
            db.commit()
            print("Livro inserido com sucesso")
            
        except Exception as e:
            # Reverter a transação em caso de erro
            db.rollback()
            print(f"Erro ao inserir livro: {e}")
    """
    def pesquisarObraPorTitulo(string: str):
        db = DatabaseManager()
        db.connect()
        try:
            # Pesquisa por título
            result = db.search_by_parameter("ObraFisica", "titulo", string)

            if result:
                obras = []
                for row in result:
                    obra = ObraFisica(row['titulo'], row['paginas'], row['data_publicacao'], row['quantidade'])
                    obras.append(obra)
                return obras
            else:
                print("Nenhuma obra encontrada com o título fornecido")
                return None
        except Exception as e:
            print(f"Erro ao pesquisar obra: {e}")
            return None
        finally:
            db.disconnect()
    """
    def pesquisarObraPorTitulo(string: str):
        db = DatabaseManager()
        db.connect()
        try:
        # Pesquisa por título na tabela ObraFisica
            result = db.search_by_parameter("ObraFisica", "titulo", string)

            if result:
                obras = []
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
                    query_livro = "SELECT * FROM Livro WHERE id = %s"
                    livro_result = db.fetch_all(query_livro, (obra_id,))

                    if livro_result:
                        print("entrou")
                        tipo = "Livro"
                        detalhes = Livro(livro_result[0]['editora'], livro_result[0]['ISBN'], livro_result[0]['genero'], '10', titulo, autores, data_publicacao, paginas, quantidade)
                        #print(detalhes.retornar_atributos())
                        obras.append(detalhes.retornar_atributos())
                    else:
                        query_periodico = "SELECT * FROM Periodico WHERE id = %s"
                        periodico_result = db.fetch_all(query_periodico, (obra_id,))
                        if periodico_result:
                            tipo = "Periodico"
                            detalhes = Periodico(periodico_result[0]['ISSN'], periodico_result[0]['editora'], periodico_result[0]['area_estudo'], periodico_result[0]['volume'])
                        else:
                            query_trabalho = "SELECT * FROM TrabalhoAcademico WHERE id = %s"
                            trabalho_result = db.fetch_all(query_trabalho, (obra_id,))
                            if trabalho_result:
                                tipo = "Trabalho Academico"
                                detalhes = TrabalhoAcademico(trabalho_result[0]['tipo'], trabalho_result[0]['orientador'], trabalho_result[0]['nivel_academico'], trabalho_result[0]['area_estudo'])
                            else:
                                detalhes = None
                
                return obras
            
            else:
                print("Nenhuma obra encontrada com o título fornecido")
                return None
        except Exception as e:
            print(f"Erro ao pesquisar obra: {e}")
            return None
        finally:
            db.disconnect()

#teste = Livro('leia','2589631456','terror','15' ,'unico2',['jorge'], '2020-04-04', 50, 5) 
#gerenciamentodados.inserirObra(teste)
results = gerenciamentodados.pesquisarObraPorTitulo('dos')
print(results)
