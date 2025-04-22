from app.models.iAnimal import iAnimal

class Animal(iAnimal):
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        self._nombre = nombre 
        self._edad = edad
        self._peso = peso
        self._kilos_comidos = 0

    def get_nombre(self) -> str:
        return self._nombre
    
    def get_edad(self) -> int:
        return self._edad
    
    def get_peso(self) -> float:
        return self._peso
    
    def comer(self, kilos_concentrado) -> None:
        self._kilos_comidos += kilos_concentrado

    def get_kilos_comidos(self) -> float:
        return self._kilos_comidos
    
    def continente_origen(self) -> str:
        return "Animal doméstico, sin origen."