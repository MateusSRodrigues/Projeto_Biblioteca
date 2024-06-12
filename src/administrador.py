from pessoa import Pessoa
import os,termios, sys, tty
import time     #apenas pra para a impressao final, retirar apos imlementar o que cada opçao faz!!!!!!!

class Administrador(Pessoa):
    def __init__(self, nome, email, cpf, endereco, saldo, senha):super().__init__(nome, email, cpf, endereco, saldo, senha)
   
    def menu(self):
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
            opcao = ["Consultar Cadastro", "Fazer reserva", "Cancelar reserva", "Fazer emprestimo", "Fazer devolucao", "Renovar emprestimo","Inserir obra", "Atualizar obra", "Excluir obra", "Procurar obra", "Calcular multa","Deletar usuario"]
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
                    if opcao[c] == opcao[0]:
                        print('esta é a opcao 1')
                        time.sleep(1000)

                else:                     #alterar o que cada opçao faz
                    if opcao [c % len(opcao)] == opcao[0]:
                        print('esta é a opcao ' + opcao[0])
                    if opcao [c % len(opcao)] == opcao[1]:
                        print('esta é a opcao ' + opcao[1])
                    if opcao [c % len(opcao)] == opcao[2]:
                        print('esta é a opcao ' + opcao[2])
                    if opcao [c % len(opcao)] == opcao[3]:
                        print('esta é a opcao ' + opcao[3])
                    if opcao [c % len(opcao)] == opcao[4]:
                        print('esta é a opcao ' + opcao[4])
                    if opcao [c % len(opcao)] == opcao[5]:
                        print('esta é a opcao ' + opcao[5])
                    if opcao [c % len(opcao)] == opcao[6]:
                        print('esta é a opcao ' + opcao[6])
                    if opcao [c % len(opcao)] == opcao[7]:
                        print('esta é a opcao ' + opcao[7])
                    if opcao [c % len(opcao)] == opcao[8]:
                        print('esta é a opcao ' + opcao[8])
                    if opcao [c % len(opcao)] == opcao[9]:
                        print('esta é a opcao ' + opcao[9])
                    if opcao [c % len(opcao)] == opcao[10]:
                        print('esta é a opcao ' + opcao[10])
                    if opcao [c % len(opcao)] == opcao[11]:
                        print('esta é a opcao ' + opcao[11])
                time.sleep(1000)
