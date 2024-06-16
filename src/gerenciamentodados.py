from db.db_managment import *
from obrafisica import ObraFisica
from livro import Livro


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
            autor_id = db.execute_query(autor_query, (Item._autor, obra_fisica_id))
            if autor_id is None:
                raise Exception("Failed to insert into Autor")

            # Inserir na tabela Livro
            livro_query = """
            INSERT INTO Livro (id, ISBN, editora, genero)
            VALUES (%s, %s, %s, %s)
            """
            livro_id = db.execute_query(livro_query, (obra_fisica_id, atributus[5],atributus[6],atributus[7]))
            if livro_id is None:
                raise Exception("Failed to insert into Livro")

            # Comitar a transação se tudo deu certo
            db.commit()
            print("Livro inserido com sucesso")
            
        except Exception as e:
            # Reverter a transação em caso de erro
            db.rollback()
            print(f"Erro ao inserir livro: {e}")

        

teste = Livro('leia','2589631456','terror','15' ,'dracarys','jorge', "2020-04-04", 50, 5) 

gerenciamentodados.inserirObra(teste)