# TP
 Esse repositório tem por finalidade criar um **Sistema de Biblioteca Avançado**, em Python, para apresentação de um trabalho em grupo de "Programação Orientada a objetos", da UFMG.

## Problema
  O sistema de Biblioteca Avançado visa abordar os desafios enfrentados por bibliotecas modernas e seus membros. Nas bibliotecas tradicionais, os processos de reserva, empréstimo e devolução de livros geralmente são manuais, consumindo tempo tanto dos membros quanto dos funcionários. Além disso, a gestão de multas e o acompanhamento do catálogo de livros podem ser complexos. À medida que as bibliotecas buscam modernizar e melhorar a experiência do usuário, o gerenciamento eficiente se torna essencial.

  Este projeto se torna importante em um contexto onde a conveniência, eficiência e acessibilidade são essenciais. O sistema aborda as necessidades tanto de membros da biblioteca quanto de funcionários, proporcionando uma experiência aprimorada no processo de busca, reserva, retirada, devolução e avaliação de livros. Além disso, a funcionalidade de gerenciamento de multas atendem a uma ampla gama de requisitos das bibliotecas, tornando-o uma solução valiosa.
Descrição

Este projeto implementa um sistema de biblioteca avançado que permite o gerenciamento de livros, periódicos, usuários, empréstimos, reservas e renovações. O sistema é baseado em classes e usa princípios de orientação a objetos para garantir modularidade e reutilização de código.

Funcionalidades

    Gerenciamento de Obras:
    Cadastro detalhado de livros e periódicos, incluindo título, autor, editora, ISBN, gênero, data de publicação, resumo, palavras-chave, quantidade de exemplares e outras informações relevantes.
    Edição de informações cadastradas, permitindo manter o acervo atualizado.
    Consulta eficiente por diversos critérios, facilitando a localização de materiais específicos.
    Exclusão segura, com mecanismos para garantir que não haja empréstimos ou reservas em aberto.
        
    Gerenciamento de Usuários:
        CCriação de perfis de usuários completos, incluindo nome, CPF, endereço, telefone, email, data de nascimento, tipo de usuário (aluno, professor, pesquisador, etc.) e outras informações relevantes.
Edição de informações cadastradas nos perfis de usuários, permitindo manter os dados atualizados.
Consulta eficiente por diversos critérios, facilitando a localização de perfis específicos.
Exclusão segura, com mecanismos para garantir que não haja empréstimos ou reservas em aberto.

    Gerenciamento de Empréstimos:
       Controle completo do processo de empréstimo, incluindo seleção de obras, verificação de disponibilidade, registro de data de empréstimo e prazo de devolução, identificação do usuário e histórico de empréstimos.
Registro de devoluções, atualizando o status das obras no sistema e notificando o usuário.
Consulta de empréstimos em andamento, com informações sobre obras emprestadas, usuários, datas de empréstimo e devolução, prazos pendentes e histórico de empréstimos.
Renovação de empréstimos dentro do período permitido e sem reservas pendentes.

    Geração de Relatórios Personalizados:
    Relatórios de obras mais emprestadas, com informações sobre quantidade de empréstimos, gênero, autor, editora e outros critérios, auxiliando na identificação de obras com maior demanda e na tomada de decisões para aquisições futuras.
    Relatórios de usuários com empréstimos em atraso, com informações sobre obras atrasadas, datas de empréstimo e devolução, prazos excedidos e histórico de empréstimos, permitindo ações de cobrança e recuperação de obras.
    Relatórios de obras mais reservadas, com informações sobre quantidade de reservas, gênero, autor, editora e outros critérios, auxiliando na identificação de obras com alta demanda e na tomada de decisões para aquisições futuras.
    
Diagrama UML

O diagrama UML do projeto, apresentado na imagem anexada, fornece uma visão detalhada das classes, seus atributos, métodos e relações entre elas. Cada classe é descrita com seus componentes e funcionalidades, demonstrando a organização e modularidade do sistema.

Tecnologias Utilizadas

    Python 3.8
    Django 3.2
    PostgreSQL 13
    Bootstrap 4.6

Requisitos de Execução

    Python 3.8 ou superior instalado
    Django 3.2 ou superior instalado
    PostgreSQL 13 ou superior instalado

Instalação

    Clonar o repositório do projeto.
    Criar um ambiente virtual.
    Ativar o ambiente virtual.
    Instalar as dependências do projeto: pip install -r requirements.txt.
    Criar um banco de dados PostgreSQL.
    Configurar o banco de dados no arquivo settings.py.
    Executar as migrações do banco de dados: python manage.py migrate.
    Executar o servidor de desenvolvimento: python manage.py runserver.

Uso

Acesse o endereço http://localhost:8000/ em um navegador web. Você poderá se cadastrar como usuário e utilizar as funcionalidades do sistema.

Documentação

A documentação completa do projeto está disponível na pasta docs.

Contribuições

Contribuições ao projeto são bem-vindas! Você pode enviar issues ou pull requests no repositório do projeto.

Contato

Para dúvidas ou sugestões, entre em contato com seu nome.
