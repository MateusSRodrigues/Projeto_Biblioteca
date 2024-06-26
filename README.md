# POO_TP_SBB

![Python](https://img.shields.io/pypi/pyversions/:packageName)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
 ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
 <h1 align="center"> TP-POO-Biblioteca </h1>
 
Esse repositório tem por finalidade criar um **Sistema de Biblioteca Básico**, em Python, para apresentação de um trabalho em grupo de "Programação Orientada a objetos", da UFMG.

## Problema
**Visão Geral:**
Este projeto se propõe a resolver problemas contemporâneos enfrentados pelas bibliotecas físicas, explorando como um Sistema de Biblioteca Avançado pode melhorar significativamente o acesso e a eficácia dessas instituições.

## Desafios atuais das Bibliotecas físicas
**As bibliotecas físicas enfrentam desafios significativos, incluindo:**
    
 * Necessidade de adaptação às expectativas dos usuários por acesso rápido e conveniente à informação digitalizada.  
 * Continuação do suporte eficaz ao acervo físico.  
 * Digitalização de informações.   
 * Mudança nos padrões de comportamento dos usuários.
    
Esses desafios exigem que as bibliotecas busquem soluções inovadoras para não apenas sobreviver, mas prosperar na era digital.
Solução Proposta: 

**Sistema de Biblioteca Básico**

O Sistema de Biblioteca Básico visa resolver esses desafios através da implementação de tecnologias modernas que facilitam a gestão de acervos híbridos, integrando eficientemente recursos físicos e digitais. As principais funcionalidades incluem:

* Gestão de Acervos Híbridos: Integração de recursos físicos e digitais para uma gestão eficiente.
* Acessibilidade à Informação: Interfaces intuitivas que proporcionam uma experiência de usuário agradável e eficaz.
* Otimização de Processos Internos: Melhoria de processos como catalogação e empréstimo.
* Serviços Personalizados: Promoção de serviços que atendam às necessidades específicas dos usuários modernos.

Objetivos do Projeto:
* Melhorar o Acesso à Informação: Facilitar o acesso tanto a recursos digitais quanto físicos.
* Aumentar a Eficiência do Trabalho: Otimizar processos internos nas bibliotecas.
* Oferecer Experiência Personalizada: Atender às necessidades específicas dos usuários com serviços personalizados.

**Resultados Esperados**

Espera-se que o projeto ofereça:
 * Análise detalhada dos desafios e oportunidades enfrentados pelas bibliotecas físicas contemporâneas.
 * Propostas de soluções concretas e viáveis.
 * Promoção de um ambiente bibliotecário mais dinâmico, acessível e eficaz.

**Conclusão**

O Sistema de Biblioteca Básico tem como objetivo principal transformar a forma como as bibliotecas físicas operam, integrando tecnologias modernas para atender às demandas da era digital. Com isso, espera-se não apenas melhorar o acesso à informação, mas também aumentar a eficácia e eficiência do trabalho realizado pelas bibliotecas.
  
  Este projeto se torna importante em um contexto onde a conveniência, eficiência e acessibilidade são essenciais. O sistema aborda as necessidades tanto de membros da biblioteca quanto de funcionários, proporcionando uma experiência aprimorada no processo de busca, devolução, etc. 

Este projeto implementa um sistema de biblioteca Básico que permite o gerenciamento de livros, periódicos, usuários, empréstimos e renovações. O sistema é baseado em classes e usa princípios de orientação a objetos para garantir modularidade e reutilização de código.

**Funcionalidades** 

O sistema de biblioteca avançado implementa as funcionalidades básicas de gerenciamento de obras, usuários e empréstimos, conforme descrito a seguir:

* Gerenciamento de Obras:
    Cadastro detalhado de livros e periódicos, incluindo título, autor, editora, ISBN, gênero, data de publicação, resumo, palavras-chave, quantidade de exemplares e outras informações relevantes.
    Edição de informações cadastradas, permitindo manter o acervo atualizado.
    Consulta eficiente por diversos critérios, facilitando a localização de materiais específicos.
    Exclusão segura, com mecanismos para garantir que não haja empréstimos em aberto.

* Gerenciamento de Usuários:
    Criação de perfis de usuários completos, incluindo nome, CPF, endereço, telefone, email, data de nascimento, tipo de usuário (aluno, professor e Administrador) e outras informações relevantes.
    Edição de informações cadastradas nos perfis de usuários, permitindo manter os dados atualizados.
    Consulta eficiente por diversos critérios, facilitando a localização de perfis específicos.
    Exclusão segura, com mecanismos para garantir que não haja empréstimos ou reservas em aberto.

* Gerenciamento de Empréstimos:
    Controle completo do processo de empréstimo, incluindo seleção de obras, verificação de disponibilidade, registro de data de empréstimo e prazo de devolução, identificação do usuário e histórico de empréstimos.
    Registro de devoluções, atualizando o status das obras no sistema e notificando o usuário.
    Consulta de empréstimos em andamento, com informações sobre obras emprestadas, usuários, datas de empréstimo e devolução, prazos pendentes e histórico de empréstimos.
    Renovação de empréstimos dentro do período permitido e sem reservas pendentes.

* Funcionalidades Aprimoradas:
Além das funcionalidades básicas, o sistema de biblioteca avançado oferece recursos aprimorados que expandem suas capacidades e o tornam uma ferramenta ainda mais completa para o gerenciamento de bibliotecas.

* Gerenciamento Avançado de Obras:
    Classificação das obras por diversos critérios (gênero, autor, editora, assunto, etc.) para facilitar a organização e a busca por materiais específicos.
    Importação e exportação de dados de obras em formatos padronizados (CSV, MARC, etc.), permitindo a integração com outros sistemas e a troca de informações.
    Controle de exemplar único para obras raras ou de valor histórico, assegurando sua preservação e disponibilidade para consulta.
    Geração de etiquetas de identificação para as obras, facilitando o controle do acervo e a organização física da biblioteca.

* Gerenciamento Avançado de Usuários:
    Definição de diferentes níveis de acesso para os usuários, permitindo controlar as funcionalidades disponíveis para cada tipo de usuário (administrador, aluno e professor).
    Integração com sistemas de autenticação externos (LDAP, Active Directory, etc.), permitindo o uso de credenciais já existentes para acessar o sistema da biblioteca.
    Geração de relatórios de uso individualizado, fornecendo informações sobre os hábitos de leitura de cada usuário e auxiliando na personalização dos serviços da biblioteca.

* Gerenciamento Avançado de Empréstimos:
    Definição de políticas de empréstimo flexíveis, permitindo configurar prazos de empréstimo, quantidade máxima de obras por usuário, renovações automáticas, multas por atrasos, etc.
    Criação de listas de espera para obras indisponíveis, notificando os usuários automaticamente quando a obra desejada estiver disponível para empréstimo.
    Geração de relatórios estatísticos sobre os empréstimos, fornecendo informações sobre a frequência de uso das obras, o perfil dos usuários e a sazonalidade da demanda.
    
## Diagrama UML
O diagrama UML do projeto, apresentado na imagem anexada, fornece uma visão detalhada das classes, seus atributos, métodos e relações entre elas. Cada classe é descrita com seus componentes e funcionalidades, demonstrando a organização e modularidade do sistema.

https://app.diagrams.net/#G10LmEIUE0eA6HMtcsmjvOs68jcEctLBKA#%7B%22pageId%22%3A%22NGueF8EDhnSrrotay3M1%22%7D 

## Tecnologias Utilizadas

 * Python 3
 * Mysql
 * Visual Studio Code

**Requisitos de Execução:**
  
 * Python 3.8 ou superior instalado
 * Banco de dados Mysql

**Instalação:**
  
  * Clonar o repositório do projeto.
  * Criar um ambiente virtual.
  * Ativar o ambiente virtual.
  * Instalar as dependências do projeto: Criar um Banco de dados e importar o o arquivo Sql no workbench 
  * Configurar o banco de dados no arquivo settings.py. 
  * Executar as migrações do banco de dados: python manage.py migrate.  
  * Executar o servidor de desenvolvimento: python manage.py runserver.

# Pré-requisitos

Para usar o sistema é preciso ter um compilador Python e um Banco de dados Mysql

# Documentação
**link:** 

https://drive.google.com/file/d/1nGauoKouBAtRJlecOfMgrgDU5LYmNK5z/view?usp=drive_link

# Ferramentas
Esse projeto utiliza as seguintes linguagens, ferramentas e bibliotecas:
   * Linguagem: [Python](https://www.python.org/downloads/)
   * Compilação: [Banco de dados Mysql](https://www.mysql.com/why-mysql/white-papers/10-principais-motivos-para-usar-o-mysql-como-um-banco-de-dados-incorporado/)
   * Visual Studio Code: [VSC](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://code.visualstudio.com/&ved=2ahUKEwju2anDuu2GAxWluZUCHdeLBUMQFnoECBQQAQ&usg=AOvVaw15O90sm1ios8AUpw56hCml)

