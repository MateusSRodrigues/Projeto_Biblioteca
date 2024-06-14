from abc import ABC, abstractmethod

class Usuario(ABC):
  
  @abstractmethod
  def deletarUsuario(self):
    pass

  @abstractmethod
  def verificarMulta(self):
    pass
    
  #abstractmethod
  #def pedirReserva(self):
  #  pass
