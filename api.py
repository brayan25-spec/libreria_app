from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

BASE_URL = "https://my-json-server.typicode.com/brayan25-spec/libreria"

# ======== Página principal ========
@app.route('/')
def home():
    return render_template('index.html')  # Carga templates/index.html

# ======== GET Y POST ========
@app.route('/api/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'GET':
        r = requests.get(f"{BASE_URL}/Libros")
        return jsonify(r.json())
    elif request.method == 'POST':
        nuevo_libro = request.json
        r = requests.post(f"{BASE_URL}/Libros", json=nuevo_libro)
        return jsonify(r.json()), r.status_code
        
@app.route('/api/estudiantes', methods=['GET', 'POST'])
def estudiantes():
    if request.method == 'GET':
        r = requests.get(f"{BASE_URL}/Estudiantes")
        return jsonify(r.json())
    elif request.method == 'POST':
        nuevo_estudiante = request.json
        r = requests.post(f"{BASE_URL}/Estudiantes", json=nuevo_estudiante)
        return jsonify(r.json()), r.status_code

@app.route('/api/estantes', methods=['GET', 'POST'])
def estantes():
    if request.method == 'GET':
        r = requests.get(f"{BASE_URL}/Estantes")
        return jsonify(r.json())
    elif request.method == 'POST':
        nuevo_estante = request.json
        r = requests.post(f"{BASE_URL}/Estantes", json=nuevo_estante)
        return jsonify(r.json()), r.status_code

@app.route('/api/prestamos', methods=['GET', 'POST'])
def prestamos():
    if request.method == 'GET':
        r = requests.get(f"{BASE_URL}/Prestamos")
        return jsonify(r.json())
    elif request.method == 'POST':
        nuevo_prestamo = request.json
        r = requests.post(f"{BASE_URL}/Prestamos", json=nuevo_prestamo)
        return jsonify(r.json()), r.status_code

if __name__ == '__main__':
    app.run(debug=True)
