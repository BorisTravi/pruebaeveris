from flask import Flask, jsonify
import socket

app = Flask(__name__)

# HelloWorld
@app.route('/greetings', methods=['GET'])
def hostname():
    host_name = socket.gethostname()
    return jsonify({'message': 'Hello World from ' + host_name})



#Potencia al cuadrado
@app.route('/square', methods=['GET'])
def cuadrado():
    number = 12
    square = 2
    return jsonify({'X': number, 'Y': square, 'resultado': number ** square},)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
