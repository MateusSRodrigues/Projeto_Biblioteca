from db.db_managment import DatabaseManager
from .obrafisica import ObraFisica
from .livro import Livro
from .periodico import Periodico
from .pessoa import Pessoa

from datetime import date, timedelta

class GerenciamentoDados:
    @staticmethod
    def inserirObra(item: ObraFisica):
        db = DatabaseManager()
        db.connect()
        db.start_transaction()
            
                # Inserir na tabela ObraFisica
        obra_fisica_query = """
                INSERT INTO ObraFisica (id, titulo, paginas, data_publicacao, quantidade)
                VALUES (%s, %s, %s, %s, %s)
                """
        obra_fisica_id = item.id
        aux=db.execute_query(obra_fisica_query, (obra_fisica_id, item.titulo, item.paginas, item.data_publicacao, item.quantidade))
        if aux == None:
            return 0

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

    @staticmethod
    def inserirCadastro(pessoa : Pessoa) -> bool:
        from .professor import Professor
        from .estudante import Estudante
        from .administrador import Administrador
        db = DatabaseManager()
        db.connect()
        try:
            
                query = """
                INSERT INTO Usuario (nome, email, cpf, endereco, senha, tipo)
                VALUES (%s, %s, %s, %s, %s, %s)
                """

            
                if isinstance(pessoa, Professor):
                    tipo = "Professor"
                elif isinstance(pessoa, Estudante):
                    tipo = "Estudante"
                elif isinstance(pessoa, Administrador):
                    tipo = "Administrador"
                
            
                params = (pessoa._nome, pessoa._email, pessoa._cpf, pessoa._endereco, pessoa._senha, tipo)
                last_row_id = db.execute_query(query, params)
                if not last_row_id:
                    print(f"Cadastro inserido com sucesso. ID: {last_row_id}")
                    return True
                else:
                    print("Erro ao inserir cadastro.")
                    return False
                
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            db.disconnect()


    @staticmethod
    def procurarCadastro(cpf_in : str) -> Pessoa:
        from .professor import Professor
        from .estudante import Estudante
        from .administrador import Administrador
        db = DatabaseManager()
        db.connect()
        try:
            query = "SELECT * FROM Usuario WHERE cpf = %s"
            result = db.fetch_one(query, (cpf_in,))
            if result:
                nome=result['nome']
                email=result['email']
                cpf=result['cpf']
                endereco=result['endereco']
                senha=result['senha']
                tipo=result['tipo']
                if tipo == 'Estudante': pessoa = Estudante(nome,email,cpf,endereco,senha)
                if tipo == 'Professor': pessoa = Professor(nome,email,cpf,endereco,senha)
                if tipo == 'Administrador': pessoa = Administrador(nome,email,cpf,endereco,senha)
            
            return pessoa
        #parei aqui
        except Exception as e:
            print(f"Erro ao procurar cadastro: {e}")
            return False
        finally:
            db.disconnect()

    def atualizar_informacoes_usuario(usuario_id, senha=None, email=None, endereco=None):
        db = DatabaseManager()
        db.connect()
        try:
            # Construir a query dinamicamente baseada nos parâmetros fornecidos
            query = "UPDATE Usuario SET "
            updates = []
            params = []

            if senha is not None:
                updates.append("senha = %s")
                params.append(senha)
            if email is not None:
                updates.append("email = %s")
                params.append(email)
            if endereco is not None:
                updates.append("endereco = %s")
                params.append(endereco)

            # Verificar se pelo menos um parâmetro foi passado
            if not updates:
                print("Nenhum dado para atualizar.")
                return False

            # Completar a query
            query += ", ".join(updates)
            query += " WHERE cpf = %s"

            # Adicionar o ID do usuário aos parâmetros
            params.append(usuario_id)

            # Executar a query
            db.execute_query(query, params)
            print("Informações do usuário atualizadas com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao atualizar informações do usuário: {e}")
            return False
        finally:
            db.disconnect()

    """
    def verificar_disponibilidade_exemplar(id_obra_fisica):
        db = DatabaseManager()
        db.connect()
        try:
            query = 
            SELECT id
            FROM Exemplar
            WHERE obra_fisica_id = %s AND estado = 'disponivel'
            LIMIT 1
            
            result = db.fetch_one(query, (id_obra_fisica,))
            return result['id'] if result else None
        except Exception as e:
            print(f"Erro ao verificar disponibilidade: {e}")
            return None
        finally:
            db.disconnect()
    """

    def registrar_emprestimo(usuario_id, obra_fisica_id):
        db = DatabaseManager()
        db.connect()
        #exemplar_id = GerenciamentoDados.verificar_disponibilidade_exemplar(obra_fisica_id)
        
        try:
                hoje = date.today()
                data_devolucao_prevista = hoje + timedelta(days=14)  # Supondo um prazo de devolução de 14 dias

                query = """
                UPDATE Exemplar
                SET estado = 'emprestado', usuario_id = %s, data_emprestimo = %s, data_devolucao_prevista = %s
                WHERE obra_fisica_id = %s AND estado = 'disponivel'
                LIMIT 1
                """
                params = (usuario_id, hoje, data_devolucao_prevista, obra_fisica_id)
                aux = db.execute_query(query, params)
                if aux :
                    print(f"Empréstimo registrado com sucesso.")
                return True
        except Exception as e:
                print(f"Erro ao registrar empréstimo: {e}")
                return False
        finally:
                db.disconnect()
      
            #print("Nenhum exemplar disponível para empréstimo.")
        #return False


    def devolver_emprestimo(usuario_id, obra_fisica_id):
        db = DatabaseManager()
        db.connect()
        #exemplar_id = GerenciamentoDados.verificar_disponibilidade_exemplar(usuario_id, obra_fisica_id)
        try:

                query = """
                    UPDATE Exemplar
                    SET estado = 'disponível', usuario_id = NULL, data_emprestimo = NULL, data_devolucao_prevista = NULL
                    WHERE cpf = %s AND obra_fisica_id = %s
                """
                params = (usuario_id, obra_fisica_id)
                aux = db.execute_query(query, params)
                if aux: 
                    print(f"Devolução registrada com sucesso.")
                return True
        except Exception as e:
                print(f"Erro ao registrar devolução: {e}")
                return False
        finally:
                db.disconnect()
        #else:
         #   print("Nenhum empréstimo encontrado para o usuário e obra especificados.")
        #return False
    
    def renovar_emprestimo(usuario_id, obra_fisica_id):
        db = DatabaseManager()
        db.connect()
        #exemplar_id = GerenciamentoDados.verificar_exemplar_emprestado(usuario_id, obra_fisica_id)
        
        #if exemplar_id:
        try:
                hoje = date.today()
                nova_data_devolucao_prevista = hoje + timedelta(days=14)  # Extensão de 14 dias

                query = """
                    UPDATE Exemplar
                    SET data_devolucao_prevista = %s
                    WHERE obra_fisica_id = %s AND cpf = %s
                """
                params = (nova_data_devolucao_prevista, obra_fisica_id, usuario_id)
                db.execute_query(query, params)
                print(f"Empréstimo renovado com sucesso. Nova data de devolução prevista: {nova_data_devolucao_prevista}")
                return True
        except Exception as e:
                print(f"Erro ao renovar empréstimo: {e}")
                return False
        finally:
                db.disconnect()
        #else:
            #print("Nenhum empréstimo encontrado para o usuário e obra especificados.")
        #return False

    def listar_emprestimo(usuario_id):
        db = DatabaseManager()
        db.connect()
        try:
            query = """
                SELECT 
                    ObraFisica.id as obra_id,
                    ObraFisica.titulo, 
                    GROUP_CONCAT(Autor.nome SEPARATOR ', ') AS autores, 
                    Exemplar.data_emprestimo, 
                    Exemplar.data_devolucao_prevista
                FROM 
                    Exemplar
                JOIN 
                    ObraFisica ON Exemplar.obra_fisica_id = ObraFisica.id
                JOIN 
                    Autor ON ObraFisica.id = Autor.obra_fisica_id
                WHERE 
                    Exemplar.usuario_id = %s AND Exemplar.estado = 'emprestado'
                GROUP BY 
                    Exemplar.id, ObraFisica.id, ObraFisica.titulo, Exemplar.data_emprestimo, Exemplar.data_devolucao_prevista
            """
            results = db.fetch_all(query, (usuario_id,))
            if results:
                emprestimos = []
                for row in results:
                    emprestimo = {
                        "obra_id": row["obra_id"],
                        "titulo": row["titulo"],
                        "autores": row["autores"],
                        "data_emprestimo": row["data_emprestimo"],
                        "data_devolucao_prevista": row["data_devolucao_prevista"]
                    }
                    emprestimos.append(emprestimo)
                    print(f"Título: {row['titulo']}")
                    print(f"Autor(es): {row['autores']}")
                    print(f"Data de Empréstimo: {row['data_emprestimo']}")
                    print(f"Data de Devolução Prevista: {row['data_devolucao_prevista']}")
                    print("\n")
                return emprestimos
            else:
                print("Nenhum empréstimo encontrado para o usuário especificado.")
                return []
        except Exception as e:
            print(f"Erro ao listar empréstimos: {e}")
            return []
        finally:
            db.disconnect()


#atualizar cadastros


#from .estudante import Estudante
# Exemplo de uso
#teste = Livro("SUMA",'9788544101002','fantasia','A guerra dos tronos',['George R.R. Martin'],'2015-06-10',688,3) 
#pessoa = Estudante('Glaucia MF','glauciaMF@ufmg.br','12345678923','Goias','mf123','2024252836')

#GerenciamentoDados.inserirCadastro(pessoa)
#GerenciamentoDados.inserirObra(teste)
#GerenciamentoDados.registrar_emprestimo(,'9788544101002')
#GerenciamentoDados.listar_emprestimo('12345678923')
"""
ISBN 978-8544101001
Autor George R.R. Martin
Titulo A guerra dos tronos - As Cronicas de Gelo e Fogo
688 
Suma

results = GerenciamentoDados.pesquisarObraPorTitulo('testinhe')
for obra in results:
    print(obra.retornar_atributos())
"""