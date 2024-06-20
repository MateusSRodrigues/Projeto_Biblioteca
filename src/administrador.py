from .pessoa import Pessoa
from .usuario import Usuario
from .livro import Livro
from .periodico import Periodico
from . import gerenciamentodados
import time

import os, termios, sys, tty
import time

#oi
class Administrador(Pessoa, Usuario):

    def __init__(self, nome, email, cpf, endereco, saldo, senha):
        super().__init__(nome, email, cpf, endereco, saldo, senha)
    '''
    def deletarUsuario(self):
        cpf = input("CPF do usuario a ser deletado")
        #chama consultacadastro() se for false volta pro menu
        #se verdadeiro chama a funçao deletar usuario do banco de dados

    def verificarMulta(self):
        input("CPF do usuario a ser deletado: ")
        #imprime resultados da funçao que calcula multa
        pass
  '''  
    def criarLivro(self) -> None:
            novo_livro = Livro()
            classe = gerenciamentodados.GerenciamentoDados()
            classe.inserirObra(novo_livro)
            pass
    
    def criarPeriodico(self):
            novo_periodico = Periodico()
            classe = gerenciamentodados.GerenciamentoDados()
            classe.inserirObra(novo_periodico)
            pass 
   
        
        
    
    def criarObra(self):
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
                        
        pass

    def procurarObra():
        os.system('clear')

        try:
            titulo = input("Insira o titulo do livro: ")
            titulo = str(titulo)
            if not titulo:
                raise ValueError("O titulo não pode ser vazio.")
            else:
                gerenciamentodados.pesquisarObraPorTitulo(titulo)
                #break
        except ValueError as e:
            print(e)
            input("Pressione enter para tentar novamente.")
            os.system("clear")


    def menuUsuario(self):
        
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
            opcao = [
                "Fazer reserva", "Cancelar reserva", "Fazer emprestimo",
                "Fazer devolucao", "Renovar emprestimo", "Inserir obra",
                "Atualizar obra", "Excluir obra", "Procurar obra",
                "Verificar multa", "Deletar usuario"
            ]
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
                    if opcao[c] == opcao[0]:  #Fazer reserva

                        print(
                            "0"
                        )  #deverá chamar a fucao fazer reserva do gerenciamento

                else:  #alterar o que cada opçao faz
                    if opcao[c % len(opcao)] == opcao[0]:  #Fazer reserva

                        print(
                            "0"
                        )  #deverá chamar a fucao fazer reserva do gerenciamento

                    if opcao[c % len(opcao)] == opcao[1]:  #Cancelar reserva

                        print(
                            "1"
                        )  #deverá chamar a fucao cancelar reserva do gerenciamento

                    if opcao[c % len(opcao)] == opcao[2]:  #Fazer emprestimo

                        print(
                            "2"
                        )  #deverá chamar a fucao fazer emprestimo do gerenciamento

                    if opcao[c % len(opcao)] == opcao[3]:  #Fazer devolucao

                        print(
                            "3"
                        )  #deverá chamar a fucao fazer devolucao do gerenciamento

                    if opcao[c % len(opcao)] == opcao[4]:  #Renovar emprestimo

                        print(
                            "4"
                        )  #deverá chamar a funcao Renovar emprestimo do gerenciamento

                    if opcao[c % len(opcao)] == opcao[5]:  #fucao inserir obra

                        #print("5")  #deverá chamar a fucao inserir obra do gerenciamento
                        self.criarObra()

                    if opcao[c % len(opcao)] == opcao[6]:  #Atualizar obra

                        print(
                            "6"
                        )  #deverá chamar a fucao Atualizar obra do gerenciamento

                    if opcao[c % len(opcao)] == opcao[7]:  #Excluir obra

                        print(
                            "7"
                        )  #deverá chamar a fucao Excluir obra do gerenciamento

                    if opcao[c % len(opcao)] == opcao[8]:  #procurar obra

                        print(
                            "8"
                        )  #deverá chamar a fucao Procurar obra do gerenciamento

                    if opcao[c % len(opcao)] == opcao[9]:  #verifica multa

                        print("9")  # self.verificaMulta()

                    if opcao[c % len(opcao)] == opcao[10]:  # Deletar usuario
                        self.deletarUsuario()
                    time.sleep(500)
                
