from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1>Hello, aaaaaa!!!!!!!</h1>"
    cursos = ['PHP', 'Java', 'C', 'Kotlin']
    data = {
        'titulo': 'Index123',
        'bienvenida': 'saludossss',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)


@app.route('/<name>/<int:edad>')
def name(name, edad):
    data = {
        'titulo': 'Index123',
        'nombre': name,
        'edad': edad
    }
    return render_template('contacto.html', data=data)


def pagina_no_encontrada(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
    # app.run(Debug=True)
