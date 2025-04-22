from app.models.animal import Animal
class Perro(Animal):

    def __init__(self, edad: str, nombre: str, peso: float, raza: str):
        super().__init__(nombre = nombre, edad = edad, peso = peso)
        self.__raza = raza

    def get_raza(self):
        return self.__raza
    
    def set_raza(self, nueva_raza):
        self.__raza = nueva_raza
    
    def emitir_sonido(self):
        return "Guau, Guau!"