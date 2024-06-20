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
      while True:
          os.system("clear")
          try:
              novo_endereco = input("Insira o novo endereço: ")
              novo_endereco = novo_endereco.lower()
 
              if not novo_endereco:
                  raise ValueError("O endereço não pode ser vazio.")

              if "rua" not in novo_endereco:
                  raise ValueError('O endereço deve conter a rua.')

              if "bairro" not in novo_endereco:
                  raise ValueError('O endereço deve conter o bairro.')

              if not any(char.isdigit() for char in novo_endereco):
                  raise ValueError('O endereço deve conter o numero da residencia')

              self.endereco = novo_endereco
              print("Endereço alterado com sucesso!")
              input("Pressione enter para voltar ao menu.")
              break

          except ValueError as e:
              print(f"Erro: {e}")
              input("Pressione enter para tentar novamente.")
  pass
  
  def atualizarEmail(self):
    while True:
        os.system("clear")
        try:
            novo_email = input("Por favor, insira o novo email: ")
            if novo_email.strip(" ") == "":
                raise ValueError("O email não pode ser vazio.")

            if not novo_email:
                raise ValueError("O email não pode ser vazio.")

            if "@" not in novo_email:
                raise ValueError('Email invalido!! Lembre-se do "@".')

            if "mail.com" not in novo_email:
                raise ValueError('Email invalido!! Lembre-se do "mail.com".')
                
            self.email = novo_email
            print("Email alterado com sucesso!")
            break

        except ValueError as e:
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente.")
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
