# APi é um lugar que disponibiliza recursos ou funcionalidades.
# 1- objetivo - criar um api que disponibiliza a consulta, criação, edição, e exculsão de livros.
# 2- URL base - localhost
# 3- Endpoints - 
#    localhost/livros (GET)
#    localhost/livros (POST)
#    localhost/livros/id (GET)
#    localhost/livros/id (PUT)
#    localhost/livros/id (DELETE)
# 4- Quais recursos
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Assasinato No Expresso Do Oriente',
        'autor': 'Agatha Christie'
    },
    {
        'id': 2,
        'título': 'Um Brinde De Cianureto',
        'autor': 'Agatha Christie'
    },
    {
        'id': 3,
        'título': 'Todas As Suas Imperfeições',
        'autor': 'Collen Hoover'
    },
]
#consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
#criar(novo)
#consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
            return jsonify(livro)
#editar
#excluir

app.run(port=5000,host ='localhost',debug=True)