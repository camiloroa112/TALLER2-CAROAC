# 1st Party Libraries
from app.models.gato import Gato
from app.models.perro import Perro
from app.models.huron import Huron
from app.models.boa_constrictor import Boa_Constrictor

# 3rd Party Libraries
import json
from flask import Flask, jsonify, render_template, request, url_for

# Instanciar Flask
app = Flask(__name__, template_folder = 'app/views', static_folder = 'app/static')

@app.route('/animals/perro', methods = ['GET'])
def get_perro():
    # Instanciando Perro
    perro = Perro(nombre = "Gauss", edad = 4, peso = 13.5, color = 'Miel', raza = "Cocker Spaniel")

    # Retornando JSON
    return jsonify({"nombre": perro.get_nombre(), "edad": perro.get_edad(), "peso": perro.get_peso(), "color": perro.get_color(), "raza": perro.get_raza(), "sonido_animal": perro.emitir_sonido()}), 200

@app.route('/animals/huron', methods = ['GET'])
def get_huron():
    # Instanciando Huron
    huron = Huron(nombre = "Albino", edad = 5, peso = 3, pais_origen = "Reino Unido", impuestos = 40)

    # Retornando JSON
    return jsonify({"nombre": huron.get_nombre(), "edad": huron.get_edad(), "peso": huron.get_peso(), "pais_origen": huron.get_pais(), 'impuestos': huron.get_impuestos(), 'sonido_animal': huron.sonido_animal(), 'flete': huron.calcular_flete()}), 200

@app.route('/animals/gato', methods = ['GET'])
def get_gato():
    # Instanciando Gato
    gato = Gato(nombre = 'Señor Gato', edad = 5, peso = 6, color = "Tri-Color", raza = "American Shorthair")

    # Retornando JSON
    return jsonify({"nombre": gato.get_nombre(), "edad": gato.get_edad(), "peso": gato.get_peso(), "color": gato.get_color(), "raza": gato.get_raza(), "sonido_animal": gato.emitir_sonido()}), 200

@app.route('/animals/boa_constrictor', methods = ['GET'])
def get_boa_constrictor():
    # Instanciando Boa
    boa = Boa_Constrictor(nombre = 'Imperator', edad = 6, peso = 89, pais_origen = 'Brasil', impuestos = 25)

    # Retornando JSON
    return jsonify({"nombre": boa.get_nombre(), "edad": boa.get_edad(), "peso": boa.get_peso(), "pais_origen": boa.get_pais(), "impuestos": boa.get_impuestos(), 'sonido_animal': boa.sonido_animal(), 'flete': boa.calcular_flete()}), 200

@app.route('/')
def home():
    # Presentando el sitio principal como animals.html
    return render_template('animals.html')

@app.route('/animals', methods = ['GET', 'POST'])
def index():
    # En caso de que el método utilizado sea GET
    if request.method == 'GET':
        return render_template('animals.html')
    
    # Para el caso de POST
    else: 
        _animal = request.form['animal'].lower()

        # Si el usuario selecciona en la lista un perro
        if _animal == 'perro':
            animal = get_perro()[0].get_json()
            img_url = url_for('static', filename='img/perro.jpg')

        # Si el usuario selecciona en la lista un huron
        elif _animal == 'huron':
            animal = get_huron()[0].get_json()
            img_url = url_for('static', filename='img/huron.jpg')

        # Si el usuario selecciona en la lista un gato
        elif _animal == 'gato':
            animal = get_gato()[0].get_json()
            img_url = url_for('static', filename='img/gato.jpg')
        
        # Si el usuario selecciona en la lista una boa
        elif _animal in ['boa', 'boa constrictor']:
            animal = get_boa_constrictor()[0].get_json()
            img_url = url_for('static', filename='img/boa.jpg')
        
        # Para cualquier otro caso
        else:
            animal = {"error": "Animal no encontrado"}

        # Visualización en la página
        return render_template('animals.html', data = json.dumps(animal, indent = 4, ensure_ascii = False), img_url = img_url, selected_animal = _animal)

# Ejecutando App
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)