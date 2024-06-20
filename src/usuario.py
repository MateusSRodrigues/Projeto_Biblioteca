from abc import ABC, abstractmethod

class Usuario(ABC):
  
    @abstractmethod
    def menuUsuario(self):
        pass
<<<<<<< HEAD

    @abstractmethod
    def deletarUsuario(self, usuario):
        pass

    @abstractmethod
    def verificarMulta(self, livro, pessoa):
        pass

    @abstractmethod
    def pedirReserva(self, pessoa, livro):
        pass

=======

    @abstractmethod
    def deletarUsuario(self, usuario):
        pass

    @abstractmethod
    def verificarMulta(self, livro, pessoa):
        pass

    @abstractmethod
    def pedirReserva(self, pessoa, livro):
        pass
>>>>>>> 498530d (atualização)
