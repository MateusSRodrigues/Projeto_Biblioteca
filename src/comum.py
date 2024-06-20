from usuario import Usuario
import os,termios, sys, tty
import time

class Comum(Usuario):

  '''def deletarUsuario(self):
      print("Usuario deletado")
      chama consultacadastro(self.CPF) se for false volta pro menu
      se verdadeiro chama a funçao deletar usuario do banco de dados
      pass

  def verificarMulta(self):
      print("sua multa é: ") #imprime resultados da funçao que calculaMulta(self.cpf)
  '''

  def ver_informacoes(self):
    os.system("clear")
    print(f'Nome: {self.nome}\nCPF: {self.CPF} \nEmail: {self.email} \nEndereço: {self.endereco}')
    input("Pressione enter.")

  pass

  def atualizarSenha(self):
    os.system("clear")
    senha_atual = input("Digite a sua senha atual: ")
    if senha_atual == self.senha:
      nova_senha = input("Digite a sua nova senha: ")
      confirma_nova_senha = input("Confirme a sua nova senha: ")
      if nova_senha == confirma_nova_senha:
        self.senha = nova_senha
        os.system("clear")
        print("Senha alterada com sucesso!!")
        input("Pressione enter.")
      else:
        os.system("clear")
        print ("As senhas nao sao iguais. Tente novamente!!")
        input("Pressione enter.")
        self.atualizarSenha()
    else:
      os.system("clear")
      print ("Senha incorreta!!")
      input("Pressione enter.")
  pass
  
  def atualizarEndereco(self):
    os.system("clear")
    self.endereco = input("Digite seu novo endereco: ")
  pass
  
  def atualizarEmail(self):
    os.system("clear")
    self.email = input("Digite seu novo Email: ")
  pass

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
          opcao = ["Ver minhas informacoes", "Listar meus emprestimos", "Atualizar senha", "Atualizar endereço", "Atualizar Email"]
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
                    self.ver_informacoes()

              else:                     #alterar o que cada opçao faz
                  if opcao [c % len(opcao)] == opcao[0]:    #Ver minhas informacoes
                    self.ver_informacoes()


                  if opcao [c % len(opcao)] == opcao[1]: #listar meus emprestimos

                      #print(opcao[0])#deverá chamar a fucao cancelar reserva do gerenciamento                        

                  if opcao [c % len(opcao)] == opcao[2]:  #Atualizar senha
                    self.atualizarSenha()

                  if opcao [c % len(opcao)] == opcao[3]: # Atualizar endereco
                    self.atualizarEndereco()
                    
                  if opcao [c % len(opcao)] == opcao[4]:  #Atualizar email
                    self.atualizarEmail()
