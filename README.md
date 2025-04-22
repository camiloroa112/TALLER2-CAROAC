# TALLER2-CAROAC

## API de Animales
Esta es una API RESTful que proporciona información sobre varios animales, incluyendo sus características y los sonidos que emiten. Está construida con Flask y permite consultar datos sobre los siguientes animales:

- Perro.
- Gato.
- Hurón.
- Boa Constrictor.

## Funcionalidades
- GET /animal/perro: Obtiene los detalles de un perro, incluyendo su nombre, edad, peso, raza y el sonido que emite.
- GET /animal/huron: Obtiene los detalles de un hurón, incluyendo su nombre, edad, peso, país de origen, impuestos y el sonido que emite.
- GET /animal/gato: Obtiene los detalles de un gato, incluyendo su nombre, edad, peso, color y el sonido que emite.
- GET /animal/boa_constrictor: Obtiene los detalles de una boa constrictora, incluyendo su nombre, edad, peso, país de origen, impuestos y el sonido que emite.

## Requisitos
Para ejecutar esta API localmente, necesitas tener instalado Python 3.x y las siguientes dependencias:

- Flask.

Para poner a prueba a la API debe tener instalado:

- Postman.

## Instalación
1. Clona este repositorio:

```
git clone https://github.com/tu_usuario/animal-api.git
cd animal-api
```

2. Crea un entorno virtual:

```
python3 -m venv venv
```

3. Activa el entorno virtual:

```
.venv\Scripts\activate
```

4. Instala las dependencias necesarias:

```
pip install -r requirements.txt
```

5. Ejecuta la aplicación Flask:

```
python api.py
```

## Endpoints
1. GET /animal/perro: Obtiene los detalles de un perro.

```
{
  "nombre": "Gauss",
  "edad": 4,
  "peso": 13.5,
  "raza": "Cocker Spaniel",
  "sonido_animal": "Guau, Guau!"
}
```

2. GET /animal/huron: Obtiene los detalles de un hurón.

```
{
  "nombre": "Albino",
  "edad": 5,
  "peso": 3,
  "pais_origen": "Reino Unido",
  "impuestos": 40,
  "sonido_animal": "¡Eek Eek!",
  "flete": 120.0
}
```

3. GET /animal/gato: Obtiene los detalles de un gato.

```
{
  "nombre": "British Shorthair",
  "edad": 5,
  "peso": 3,
  "sonido": "Miau, Miau!",
  "color": "Negro"
}
```

4. GET /animal/boa_constrictor: Obtiene los detalles de una boa constrictor.

```
{
  "nombre": "Imperator",
  "edad": 6,
  "peso": 89,
  "pais_origen": "Brasil",
  "color": 25,
  "sonido_animal": "¡Tsss!",
  "flete": 2225.0
}
```