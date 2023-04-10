from flask import Flask, jsonify, request

app = Flask(__name__)

# definimos una ruta
@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

# definimos otra ruta y un método POST
@app.route('/suma', methods=['POST'])
def suma():
    # obtenemos los valores enviados en el cuerpo de la petición
    valores = request.get_json()
    # realizamos la suma de los valores
    resultado = sum(valores)
    # devolvemos el resultado como un JSON
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
