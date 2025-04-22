from typing import Union
from app.models.huron import Huron
from app.models.boa_constrictor import Boa_Constrictor

class Guarderia:
    def __init__(self):
        self.__huron1 = Huron(nombre = 'Albino', edad = 4, peso = 10, pais_origen = 'Sudafrica', impuestos = 0.15)
        self.__huron2 = Huron(nombre = 'Canela', edad = 5, peso = 14, pais_origen = 'Congo', impuestos = 0.22)
        self.__boa1 = Boa_Constrictor(nombre = 'Sabogae', edad = 7, peso = 80, pais_origen = 'Brasil', impuestos = 0.3)
        self.__boa2 = Boa_Constrictor(nombre = 'Imperator', edad = 10, peso = 100, pais_origen = 'China', impuestos = 0.35)

    def alimentar_boa(self, boa: Union[Boa_Constrictor, None], raton_comido: int):
        """Method to feed of more rats to boas"""
        
        # Verifying if the Boa exists
        if boa is None:
            return "¡Esta Boa no existe!"
        
        else:

            # Attempting to feed Boa
            try:
                boa.comer(raton_comido = raton_comido)

            # Displaying error 
            except ValueError as e:
                print(f'La boa ha comido hasta el momento: {boa.get_ratones_comidos()} {e}')

            # In case the process was successful
            else: 
                print("Éxito")

            # Displaying end of the process message
            finally:
                print('Proceso finalizado.')

    def get_boa1(self):
        """Method to return the first Boa class."""
        return self.__boa1
    
    def get_boa2(self):
        """Method to return the second Boa class."""
        return self.__boa2
    
    def get_huron1(self):
        """Method to return the first Huron class."""
        return self.__huron1
    
    def get_huron2(self):
        """Method to return the second Huron class."""
        return self.__huron2