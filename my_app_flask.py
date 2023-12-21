"""
Meu primeiro app com Flask
"""
from flask import Flask


# Herdando a biblioteca Flask na variável my_app_flask
my_app_flask = Flask(__name__)
# Definindo a rota inicial index.html
@my_app_flask.route("/<string:passagem_de_paramentros_via_uri>", methods=['GET', 'POST'])
# Definindo a função da index.html
def index(passagem_de_paramentros_via_uri):
    """
    Criando a página index.html
    """
    return f"Hello World {passagem_de_paramentros_via_uri}"

if __name__ == "__main__":
    my_app_flask.run(debug=True)
