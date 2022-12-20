#1. objetivo
#2. Url base (host)
#3. endpoint
    # - localhost/livros (GET)
    # - localhost/livros/id (GET)
    # - localhost/livros    (POST)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)
#4. quais recursos?
    #livros

from flask import Flask, jsonify, request

app = Flask(__name__)



climatempo = [
    {
        'id' : 1,
        'Região' : 'Sudeste',
        'Temperatura' : 25
    },
    {
        'id' : 2,
        'Região' : 'Sul',
        'Temperatura' : 18
    }
]

@app.route('/tempo', methods = ['GET'])
def obter_clima():
    return jsonify(climatempo)

app.run(port=4000,host='localhost',debug=True)