from app.models.animal import Animal
class Animal_Exotico(Animal):
    def __init__(self, nombre: str, edad: str, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre = nombre, edad = edad, peso = peso)
        self._impuestos = impuestos
        self._pais_origen = pais_origen
    
    def calcular_flete(self) -> float:
        return round(self._impuestos * self._peso, 2)
    
    def get_impuestos(self) -> float: 
        return self._impuestos
    
    def get_pais(self) -> str:
        return self._pais_origen