from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'titulo': 'Index',
        'encabezado': 'Bienvenido(a)'
    }
    return render_template('index.html', data=data)

@app.route('/holaMundo')
def hola_mundo():
    return "Hola Mundo!"

if __name__ == '__main__':
    app.run(debug=True, port=5005)