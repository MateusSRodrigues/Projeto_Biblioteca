from pessoa import Pessoa
import os,termios, sys, tty

class Administrador(Pessoa):
    def __init__():super().__init__(nome, email, cpf, endereco, saldo, senha)
        def get_char():
    # Função para capturar o caractere pressionado pelo usuário
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def menu2(opcao, cabecalho):
    c = 0
    while True:
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
                return opcao[0]
            else:
                return opcao[c % len(opcao)]
