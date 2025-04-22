from app.models.animal import Animal
class Gato(Animal):

    def __init__(self, nombre: str, edad: int, peso: float, color: str):
        super().__init__(nombre = nombre, edad = edad, peso = peso)
        self.__color = color
    
    def get_color(self):
        return self.__color
    
    def set_color(self, nuevo_color: str):
        self.__color = nuevo_color

    def emitir_sonido(self):
        return "Miau, Miau!"