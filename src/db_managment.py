import mysql.connector
from mysql.connector import Error


# Database connection details (adjust if needed)
db_connection = {
    'host': 'localhost',  # Seu endereço IPv4 do WSL
    'user': 'mateus',
    'password': '264859',
    'database': 'biblioteca',
}

def create_obra(titulo, paginas, data_publicacao, quantidade):
    try:
        # Conectando ao banco de dados
        connection = mysql.connector.connect(**db_connection)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Inserir dados na tabela ObraFisica
            query = """
            INSERT INTO ObraFisica (titulo, paginas, data_publicacao, quantidade)
            VALUES (%s, %s, %s, %s)
            """
            valores = (titulo, paginas, data_publicacao, quantidade)
            
            cursor.execute(query, valores)
            connection.commit()
            
            # Obtendo o ID da obra inserida
            obra_id = cursor.lastrowid
            
            print("Obra inserida com sucesso!")
            
            return obra_id
    
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_autor(nome, obra_fisica_id):

    try:
        # Conectando ao banco de dados
        connection = mysql.connector.connect(**db_connection)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Inserir dados na tabela ObraFisica
            query = """
            INSERT INTO Autor (nome, obra_fisica_id) VALUES (%s, %s)
            """
            valores = (nome, obra_fisica_id)
            
            cursor.execute(query, valores)
            connection.commit()
            
            
            print("Autor inserido com sucesso!")
            
    
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_livro(id, isbn, editora, genero):
    try:
        # Conectando ao banco de dados
        connection = mysql.connector.connect(**db_connection)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Inserir dados na tabela ObraFisica
            query = """
            INSERT INTO Livro (id, ISBN, editora, genero) VALUES (%s, %s, %s, %s)
            """
            valores = (id, isbn, editora, genero)
            
            cursor.execute(query, valores)
            connection.commit()
            
            
            print("Livro inserido com sucesso!")
            
    
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#def creat_periodico():

#def create_trabalhoacademico():

def listar_todas_obras():
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**db_connection)
        cursor = conn.cursor()

        # Executa a consulta para listar todas as obras
        cursor.execute("SELECT * FROM ObraFisica")

        # Obtém todos os resultados da consulta
        obras = cursor.fetchall()

        # Cabeçalhos das colunas
        colunas = [desc[0] for desc in cursor.description]

        # Exibe os resultados
        for coluna in colunas:
            print(f"{coluna}\t", end="")
        print()
        
        for obra in obras:
            for item in obra:
                print(f"{item}\t", end="")
            print()
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    
    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()

def buscar_obras_por_titulo(titulo_busca):

    conn = mysql.connector.connect(**db_connection)
    cursor = conn.cursor()

    # Monta a consulta SQL
    query = "SELECT * FROM ObraFisica WHERE titulo LIKE %s"
    like_pattern = f"%{titulo_busca}%"

    # Executa a consulta
    cursor.execute(query, (like_pattern,))

    # Busca os resultados
    resultados = cursor.fetchall()

    # Fecha a conexão
    cursor.close()
    conn.close()

    return resultados

print(buscar_obras_por_titulo("dos"))

def delete_autor(autor_id):
    db = db_connection()
    cursor = db.cursor()
    sql = "DELETE FROM Autor WHERE id = %s"
    val = (autor_id,)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()

def get_autor_by_id(autor_id):
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Autor WHERE id = %s", (autor_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def get_all_autores():
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Autor")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def update_autor(autor_id, nome, obra_fisica_id):
    db = db_connection()
    cursor = db.cursor()
    sql = "UPDATE Autor SET nome = %s, obra_fisica_id = %s WHERE id = %s"
    val = (nome, obra_fisica_id, autor_id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()



num = create_obra('O principe', 1178, '1954-07-29', 10)
print(f"id da obra{num}")
create_autor("Maquiavel",num)
create_livro(num,9788656510785, 'suma', 'fantasia')
#inserir_obra('A Furia dos Reis', 1178, '1954-07-29', 10)
#inserir_obra('O Festim dos Corvos', 1178, '1954-07-29', 10)
#inserir_obra('A Tormenta de Espadas', 1178, '1954-07-29', 10)
#inserir_obra('A Dança dos Dragoes', 1178, '1954-07-29', 10)
#listar_todas_obras()
#print(buscar_obras_por_titulo("dos"))
