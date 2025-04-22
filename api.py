# 1st Party Libraries
from app.models.gato import Gato
from app.models.perro import Perro
from app.models.huron import Huron
from app.models.boa_constrictor import Boa_Constrictor

# 3rd Party Libraries
from flask import Flask, jsonify, request

# Instanciar Flask
app = Flask(__name__)

@app.route('/animal/perro', methods = ['GET'])
def get_perro():
    # Instanciando Perro
    perro = Perro(nombre = "Gauss", edad = 4, peso = 13.5, raza = "Cocker Spaniel")

    # Retornando JSON
    return jsonify({"nombre": perro.get_nombre(), "edad": perro.get_edad(), "peso":perro.get_peso(), "raza": perro.get_raza(), "sonido_animal": perro.emitir_sonido()}), 200

@app.route('/animal/huron', methods = ['GET'])
def get_huron():
    # Instanciando Huron
    huron = Huron(nombre = "Albino", edad = 5, peso = 3, pais_origen = "Reino Unido", impuestos = 40)

    # Retornando JSON
    return jsonify({"nombre": huron.get_nombre(), "edad": huron.get_edad(), "peso": huron.get_peso(), "pais_origen": huron.get_pais(), 'impuestos': huron.get_impuestos(), 'sonido_animal': huron.sonido_animal(), 'flete': huron.calcular_flete()}), 200

@app.route('/animal/gato', methods = ['GET'])
def get_gato():
    # Instanciando Gato
    gato = Gato(nombre = "British Shorthair", edad = 5, peso = 3, color = "Negro")

    # Retornando JSON
    return jsonify({"nombre": gato.get_nombre(), "edad": gato.get_edad(), "peso": gato.get_peso(), "sonido": gato.emitir_sonido(), "color": gato.get_color()}), 200

@app.route('/animal/boa_constrictor', methods = ['GET'])
def get_boa_constrictor():
    # Instanciando Boa
    boa = Boa_Constrictor(nombre = 'Imperator', edad = 6, peso = 89, pais_origen = 'Brasil', impuestos = 25)

    # Retornando JSON
    return jsonify({"nombre": boa.get_nombre(), "edad": boa.get_edad(), "peso": boa.get_peso(), "pais_origen": boa.get_pais(), "color": boa.get_impuestos(), 'sonido_animal': boa.sonido_animal(), 'flete': boa.calcular_flete()}), 200

@app.route('/')
def home():
    return "Bienvenido a la API de animales."

# Ejecutando App
if __name__ == "__main__":
    app.run(debug = True)