from pessoa import Pessoa
import os,termios, sys, tty
import time

class Administrador(Pessoa):
    def __init__(self, nome, email, cpf, endereco, saldo, senha):super().__init__(nome, email, cpf, endereco, saldo, senha)

    def deletarUsuario(self):
        input("CPF do usuario a ser deletado")
        #chama consultacadastro() se for false volta pro menu
        #se verdadeiro chama a funçao deletar usuario do banco de dados
   
    def menuUsuario(self):
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
            opcao = ["Fazer reserva", "Cancelar reserva", "Fazer emprestimo", "Fazer devolucao", "Renovar emprestimo","Inserir obra", "Atualizar obra", "Excluir obra", "Procurar obra", "Calcular multa", "Deletar usuario"]
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
                    if opcao[c] == opcao[0]: #Fazer reserva
                        
                        #deverá chamar a fucao fazer reserva do gerenciamento
                     

                else:                     #alterar o que cada opçao faz
                    if opcao [c % len(opcao)] == opcao[0]:    #Fazer reserva

                        #deverá chamar a fucao fazer reserva do gerenciamento
                        
                        
                    if opcao [c % len(opcao)] == opcao[1]: #Cancelar reserva
                        
                        #deverá chamar a fucao cancelar reserva do gerenciamento

                        
                    if opcao [c % len(opcao)] == opcao[2]: #Fazer emprestimo

                         #deverá chamar a fucao fazer emprestimo do gerenciamento 
                        
                    if opcao [c % len(opcao)] == opcao[3]: #Fazer devolucao
                        
                    #deverá chamar a fucao fazer devolucao do gerenciamento

                    
                    if opcao [c % len(opcao)] == opcao[4]: #Renovar emprestimo
                        
                    #deverá chamar a funcao Renovar emprestimo do gerenciamento

                    
                    if opcao [c % len(opcao)] == opcao[5]: #fucao inserir obra
                        
                     #deverá chamar a fucao inserir obra do gerenciamento  
                        
                    if opcao [c % len(opcao)] == opcao[6]: #Atualizar obra
                        
                    #deverá chamar a fucao Atualizar obra do gerenciamento   

                    
                    if opcao [c % len(opcao)] == opcao[7]: #Excluir obra
                        
                    #deverá chamar a fucao Excluir obra do gerenciamento    

                    
                    if opcao [c % len(opcao)] == opcao[8]: #procurar obra
                        
                    #deverá chamar a fucao Procurar obra do gerenciamento                        

                        
                    if opcao [c % len(opcao)] == opcao[9]:  #Calcular multa
                        
                        print('esta é a opcao ' + opcao[9]) #deve calcular e imorimir a multa?

                    
                    if opcao [c % len(opcao)] == opcao[9]:  Deletar usuario
                        self.deletarUsuario()
                    
