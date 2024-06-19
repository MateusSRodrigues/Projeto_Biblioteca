from usuario import Usuario
import os,termios, sys, tty

class Comum(Usuario):

  def deletarUsuario(self):
      print("Usuario deletado")
      #chama consultacadastro(self.CPF) se for false volta pro menu
      #se verdadeiro chama a funçao deletar usuario do banco de dados
      pass

  def verificarMulta(self):
      print("sua multa é: ") #imprime resultados da funçao que calculaMulta(self.cpf)


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
          opcao = ["Fazer reserva", "Cancelar reserva", "Verificar multa", "Deletar usuario"]
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

                       print(opcao[0])#deverá chamar a fucao fazer reserva do gerenciamento


              else:                     #alterar o que cada opçao faz
                  if opcao [c % len(opcao)] == opcao[0]:    #Fazer reserva

                      print(opcao[0])#deverá chamar a fucao fazer emprestimo do gerenciamento 
#deverá chamar a fucao fazer reserva do gerenciamento


                  if opcao [c % len(opcao)] == opcao[1]: #Cancelar reserva

                      print(opcao[0])#deverá chamar a fucao cancelar reserva do gerenciamento                        

                  if opcao [c % len(opcao)] == opcao[2]:  #verifica multa

                      print(opcao[1]) #self.verificaMulta()

                  if opcao [c % len(opcao)] == opcao[3]: # Deletar usuario
                      
                      print(opcao[2]) #self.deletarUsuario()