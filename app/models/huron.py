from app.models.animal_exotico import Animal_Exotico
class Huron(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)

    def sonido_animal(self) -> str:
        return "¡Eek Eek!"