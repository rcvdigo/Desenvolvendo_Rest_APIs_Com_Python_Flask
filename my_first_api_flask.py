"""
Minha primeira API com flask
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask import json


# Criando uma instância da aplicação Flask
my_app_flask = Flask(__name__)

@my_app_flask.route("/<int:person_id>", methods=['GET'])
def index(person_id):
    """
    Rota: /<int:person_id>
    Método: GET
    Descrição: Retorna informações sobre uma pessoa com o ID especificado.

    Parâmetros:
    - person_id (int): O ID da pessoa.

    Retorno:
    Um objeto JSON contendo as informações da pessoa.
    """
    return jsonify({'id': person_id,
                    'nome': 'Rodrigo',
                    'profissao': 'Desenvolvedor'})


@my_app_flask.route("/soma_get/<int:valor1>/<int:valor2>/", methods=['GET'])
def soma_get(valor1, valor2):
    """
    Rota: /soma_get/<int:valor1>/<int:valor2>/
    Método: GET
    Descrição: Realiza a soma de dois valores passados via URI.

    Parâmetros:
    - valor1 (int): O primeiro valor.
    - valor2 (int): O segundo valor.

    Retorno:
    Um objeto JSON contendo o resultado da soma.
    """
    return jsonify({'soma': valor1 + valor2})


@my_app_flask.route("/soma_post/", methods=['POST', 'PUT'])
def soma_post():
    """
    Rota: /soma_post/
    Métodos: POST, PUT
    Descrição: Realiza a soma de valores passados no corpo da requisição.

    Entrada:
    - Um objeto JSON contendo a lista de valores a serem somados.

    Retorno:
    Um objeto JSON contendo o resultado da soma.
    """
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma': total})


@my_app_flask.route("/soma_post_get/", methods=['POST', 'GET'])
def soma_post_get():
    """
    Rota: /soma_post_get/
    Métodos: POST, GET
    Descrição: Realiza a soma de valores, 
    sendo por POST com dados no corpo ou por GET com valores fixos.

    Entrada (POST):
    - Um objeto JSON contendo a lista de valores a serem somados.

    Retorno:
    Um objeto JSON contendo o resultado da soma.
    """
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})


if __name__ == "__main__":
    # Inicia a aplicação em modo de depuração
    my_app_flask.run(debug=True)
