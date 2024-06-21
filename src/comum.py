from .usuario import Usuario
from .pessoa import Pessoa
import os,termios, sys, tty
import time

class Comum(Usuario):

    def ver_informacoes(pessoa : Pessoa) -> None:
        os.system("clear")
        print(f'Nome: {pessoa.nome}\nCPF: {pessoa.cpf} \nEmail: {pessoa.email} \nEndereço: {pessoa.endereco}')
        input("Pressione enter.")

    def atualizarSenha(pessoa : Pessoa) -> None:
        os.system("clear")
        senha_atual = input("Digite a sua senha atual: ")
      
        
        while True:
            if senha_atual == pessoa.senha:
                try:
                    nova_senha = input("Digite a sua nova senha: ")
                    if not nova_senha:
                        raise ValueError("A senha não pode ser vazia.")
                    if ' ' in nova_senha:
                        raise ValueError("A senha não pode ter espaco")
                    else:
                        break
                except ValueError as e:
                    print(e)
                    input("Pressione enter para tentar novamente.")
                    os.system("clear")

                confirma_nova_senha = input("Confirme a sua nova senha: ")
                if nova_senha == confirma_nova_senha:
                    from gerenciamentodados import GerenciamentoDados
                    pessoa.senha = nova_senha
                    os.system("clear")
                    print("Senha alterada com sucesso!!")
                    GerenciamentoDados.atualizar_informacoes_usuario(pessoa.cpf,nova_senha,None,None)
                    input("Pressione enter.")
                    time.sleep(5)
                    
                else:
                    os.system("clear")
                    print ("As senhas nao sao iguais. Tente novamente!!")
                    input("Pressione enter.")
                    Comum.atualizarSenha()
            else:
                os.system("clear")
                print ("Senha incorreta!!")
                input("Pressione enter.")
  
  
    def atualizarEndereco(pessoa : Pessoa) -> None:
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

              pessoa.endereco = novo_endereco
              from gerenciamentodados import GerenciamentoDados
              GerenciamentoDados.atualizar_informacoes_usuario(pessoa.cpf,None,None,novo_endereco)
              print("Endereço alterado com sucesso!")
              input("Pressione enter para voltar ao menu.")
            
              break

          except ValueError as e:
              print(f"Erro: {e}")
              input("Pressione enter para tentar novamente.")
  
  
    def atualizarEmail(pessoa : Pessoa) -> None:
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
                    
                pessoa.email = novo_email
                from gerenciamentodados import GerenciamentoDados
                GerenciamentoDados.atualizar_informacoes_usuario(pessoa.cpf,None,novo_email,None)
                print("Email alterado com sucesso!")
                break

            except ValueError as e:
                print(f"Erro: {e}")
                input("Pressione enter para tentar novamente.")

    def listarEmprestimo(pessoa : Pessoa) -> None:
        from .gerenciamentodados import GerenciamentoDados
        GerenciamentoDados.listar_emprestimo(pessoa.cpf)
        time.sleep(10)

    
    def procurarObra() -> None:
            os.system('clear')
            from .sistema import Sistema
            Sistema.procurarObra()

    def menuUsuario(pessoa : Pessoa) -> None:
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
          elif n == 'd':  # escolhe opçãos
              if c == 0:
                  if opcao[c] == opcao[0]: #Fazer reserva
                    Comum.ver_informacoes(pessoa)

              else:                     #alterar o que cada opçao faz
                  if opcao [c % len(opcao)] == opcao[0]:    #Ver minhas informacoes
                    Comum.ver_informacoes(pessoa)


                  if opcao [c % len(opcao)] == opcao[1]: #listar meus emprestimos
                    Comum.listarEmprestimo(pessoa)
                      #print(opcao[0])#deverá chamar a fucao cancelar reserva do gerenciamento                        

                  if opcao [c % len(opcao)] == opcao[2]:  #Atualizar senha
                    Comum.atualizarSenha(pessoa)

                  if opcao [c % len(opcao)] == opcao[3]: # Atualizar endereco
                    Comum.atualizarEndereco(pessoa)
                    
                  if opcao [c % len(opcao)] == opcao[4]:  #Atualizar email
                    Comum.atualizarEmail(pessoa)

