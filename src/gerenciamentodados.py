from db_managment import * 
from obrafisica import ObraFisica
from livro import Livro


class gerenciamentodados():
    def inserirObra(Item : ObraFisica):
        id = create_obra(Item._titulo, Item._paginas, Item._data_publicacao, Item._quantidade)
        if isinstance(Item, Livro):
            atributus = Item.retornar_atributos()
            create_livro(id,atributus[0],atributus[1],atributus[2])
        

teste = Livro('livro teste','joao', '2020/04/04/', 50, 5, 3, 'novo',2589631456, 'suma', 'fantasia', 15 )
gerenciamentodados.inserirObra(teste)