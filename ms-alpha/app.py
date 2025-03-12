from main import create_app, db, circuit_breaker
import time

app = create_app()

app.app_context().push()

@app.route('/healthcheck')
def healthcheck():
    return 'App working correctly!', 200

@app.route('/compras')
def compras():
    time.sleep(3)
    compras = [{
        'id': 1,
        'nombre': 'Arroz',
        'cantidad': 1,
        'precio': 2.50
    }, {
        'id': 2,
        'nombre': 'Leche',
        'cantidad': 2,
        'precio': 1.50
    }, {
        'id': 3,
        'nombre': 'Papa',
        'cantidad': 3,
        'precio': 0.50
    }]
    return compras, 200

@app.route('/simulate-failure')
@circuit_breaker
def simulate_failure():
    # simular una falla
    # Por ejemplo vamos a intentar acceder a una variable que no existe
    resutl = variable_que_no_existe # Esto va a causar un NnameError
    return 'Esta linea nunca se va a ejecutar si ocurre el error, o si tengo una falla antes', 200

@app.route('/no-failure')
@circuit_breaker
def no_failure():
    items = [{
        'id': 1,
        'nombre': 'Arroz',
        'cantidad': 1,
        'precio': 2.50
    }, {
        'id': 2,
        'nombre': 'Leche',
        'cantidad': 2,
        'precio': 1.50
    }]
    return items, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)