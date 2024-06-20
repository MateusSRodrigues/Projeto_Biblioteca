from .obrafisica import ObraFisica
from .gerenciamentodados import GerenciamentoDados
from .pessoa import Pessoa
import os,termios, sys, tty
import time

class Sistema:
    def login(self):
        cpf = input("CPF: ")
        senha = input("Senha: ")
        #chama a funçao que consultarcadastro(cpf,senha)
        # if "funcao consultar cadastro" retornar false chama menu inicial de novo
        # else cria uma pessoa(adm,graduando...) e chama a sua funcao menu 
    

    def cadastrar(self):
        pessoa = Pessoa()
        GerenciamentoDados.inserirCadastro(pessoa)
    

    def menuInicial(self):
        def get_char():        # Função para capturar o caractere pressionado pelo usuário
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
            opcao = ["Login", "Cadastrar", "Pesquisar obra"]
            cabecalho = ["Pressione 'W' para subir 'S' para descer e 'D' para selecionar.\n", "O que deseja Fazer?"]
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
                    print("====================================\n====================================")

            n = get_char()

            if n == 's':
                c += 1  # altera contador de click, desce a seta
            elif n == 'w':
                c -= 1  # altera contador de click, sobe a seta
            elif n == 'd':  # escolhe opção
                if c == 0:
                    if opcao[c] == opcao[0]: #Login
                        self.login()

                else:                     #alterar o que cada opçao faz
                    if opcao [c % len(opcao)] == opcao[0]: #Login   
                        self.login()

                    
                    if opcao [c % len(opcao)] == opcao[1]: #Cadastrar
                        self.cadastrar()
                    
                    if opcao [c % len(opcao)] == opcao[2]: #Pesquisar obra
                       #chama a funcao pesquisar obra do banco de dados
                        titulo = input(print("Digite o titulo da obra:"))
                        aux = GerenciamentoDados.pesquisarObraPorTitulo(titulo)
                        result = self.selecionar(aux)
                        print(result.retornar_atributos())

                        time.sleep(500)

    def selecionar(self, lista: list[ObraFisica]):
        for index, obra in enumerate(lista, start=1):
            print(f"{index}: {obra.titulo}, {obra.autor}")
        
        indice = int(input(print("Escolha a obra pelo numero indexado:")))
        if 1 <= indice <= len(lista):
            return lista[indice - 1]
        else:
            raise IndexError("Índice fora do intervalo válido")
        

#teste = Sistema()
#teste.menuInicial()
