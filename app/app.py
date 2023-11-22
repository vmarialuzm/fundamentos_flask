from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():
    print('Antes de la petición...')

@app.after_request
def after_request(response):
    print('Después de la petición...')
    return response

@app.route('/')
def index():
    print('Estamos realizando la petición...')
    data = {
        'titulo': 'Index',
        'encabezado': 'Bienvenido(a)'
    }
    return render_template('index.html', data=data)

@app.route('/contacto')
def contacto():
    data = {
        'titulo': 'Contacto',
        'encabezado': 'Bienvenido(a)'
    }
    return render_template('contacto.html', data=data)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return '¡Hola, {0}!'.format(nombre)

@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return 'La suma es: {0}'.format((valor1 + valor2))

@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return 'Tu nombre es: {0} y tu edad es: {1}'.format(nombre, edad)

@app.route('/lenguajes')
def lenguajes():
    data={
        'hay_lenguajes': False,
        'lenguajes':['PHP', 'Python', 'Kotlin', 'Java', 'C#', 'Javascript']
    }
    return render_template('lenguajes.html', data=data)

@app.route('/datos')
def datos():
    print(request.args)
    a = request.args.get('valor1')
    b = int(request.args.get('valor2'))
    return 'Estos son los datos: {0}, {1}'.format(a, (b+15))

@app.route('/holaMundo')
def hola_mundo():
    return "Hola Mundo!"

if __name__ == '__main__':
    app.run(debug=True, port=5005)