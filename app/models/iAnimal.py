from abc import ABC, abstractmethod
class iAnimal(ABC):
    
    @abstractmethod # Interface
    def comer(self, kilos_concentrado):
        pass

    @abstractmethod # Abstract Method 1
    def get_kilos_comidos(self):
        pass
    
    @abstractmethod # Abstract Method 2
    def continente_origen(self):
        pass