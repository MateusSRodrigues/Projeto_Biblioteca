from .pessoa import Pessoa
from .usuario import Usuario
from .livro import Livro
from .periodico import Periodico

import os, termios, sys, tty
import time

class Administrador(Pessoa, Usuario):

    def __init__(self, nome, email, cpf, endereco, senha):
        super().__init__(nome, email, cpf, endereco, senha)


    def criarLivro(self) -> None:
            from gerenciamentodados import GerenciamentoDados
            novo_livro = Livro()
            classe = GerenciamentoDados()
            classe.inserirObra(novo_livro)
        
    
    def criarPeriodico(self) -> None:
            from gerenciamentodados import GerenciamentoDados
            novo_periodico = Periodico()
            classe = GerenciamentoDados()
            classe.inserirObra(novo_periodico)
            
   
        
        
    
    def criarObra(self) -> None:
        def get_char():  # Função para capturar o caractere pressionado pelo usuário
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

        c = 0
        while True:
            opcao = ["Livro", "Periodico"]
            cabecalho = [
                "Pressione 'W' para subir 'S' para descer e 'D' para selecionar.\n",
                "Qual tipo de obra deseja inserir?"
            ]
            os.system('clear')
            os.system('cls' if os.name == 'nt' else 'clear')

            for i in range(len(opcao)):
                if i == 0:
                    for item in cabecalho:
                        print(item, end='')
                    print("\n------------------------------")
                if i == c % len(opcao):
                    print(f"->{opcao[i]}")
                else:
                    print(opcao[i])
                if i == len(opcao) - 1:
                    print(
                        "====================================\n===================================="
                    )

            n = get_char()

            if n == 's':
                c += 1  # altera contador de click, desce a seta
            elif n == 'w':
                c -= 1  # altera contador de click, sobe a seta
            elif n == 'd':  # escolhe opção
                if c == 0:
                    if opcao[c] == opcao[0]:  #Livro
                          self.criarLivro()
                          
                else:  #alterar o que cada opçao faz
                    if opcao[c % len(opcao)] == opcao[0]:  #Livro
                        self.criarLivro()

                    if opcao[c % len(opcao)] == opcao[1]:  #Periodico
                        self.criarPeriodico()
                        
        

    def procurarObra() -> None:
        os.system('clear')
        from .sistema import Sistema
        Sistema.procurarObra()


    def menuUsuario(self) -> None:
        from .gerenciamentodados import GerenciamentoDados
        from .sistema import Sistema
        
        def get_char():  # Função para capturar o caractere pressionado pelo usuário
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

        c = 0
        while True:
            opcao = ["Fazer emprestimo", "Renovar emprestimo","Fazer devolucao", "Procurar obra", "Inserir obra"]
            cabecalho = [
                "Pressione 'W' para subir 'S' para descer e 'D' para selecionar.\n",
                "O que deseja Fazer?"
            ]
            os.system('clear')
            os.system('cls' if os.name == 'nt' else 'clear')

            for i in range(len(opcao)):
                if i == 0:
                    for item in cabecalho:
                        print(item, end='')
                    print("\n------------------------------")
                if i == c % len(opcao):
                    print(f"->{opcao[i]}")
                else:
                    print(opcao[i])
                if i == len(opcao) - 1:
                    print(
                        "====================================\n===================================="
                    )

            n = get_char()

            if n == 's':
                c += 1  # altera contador de click, desce a seta
            elif n == 'w':
                c -= 1  # altera contador de click, sobe a seta
            elif n == 'd':  # escolhe opção
                if c == 0:
                    if opcao[c] == opcao[0]:  #Fazer emprestimo

                        print(
                            "0"
                        )  #deverá chamar a fucao fazer reserva do gerenciamento

                else:  #alterar o que cada opçao faz
                    if opcao[c % len(opcao)] == opcao[0]:  #Fazer emprestimo

                        print("0")  #deverá chamar a fucao fazer reserva do gerenciamento

                    if opcao[c % len(opcao)] == opcao[1]:  #Renovar emprestimo

                        print("1")  #deverá chamar a fucao cancelar reserva do gerenciamento

                    if opcao[c % len(opcao)] == opcao[2]:  #Fazer devolucao

                        print("2")  #deverá chamar a fucao fazer emprestimo do gerenciamento
                        
                    if opcao[c % len(opcao)] == opcao[3]:  #procurar obra

                        titulo = input(print("Digite o titulo da obra:"))
                        aux = GerenciamentoDados()
                        aux.pesquisarObraPorTitulo(titulo)
                        result = Sistema.selecionar(aux)
                        print(result.retornar_atributos())    

                    if opcao[c % len(opcao)] == opcao[4]:  #fucao inserir obra

                        self.criarObra()

                    time.sleep(500)
                

