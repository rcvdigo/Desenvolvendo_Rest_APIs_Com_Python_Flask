"""
Minha primeira APIRESTFUL com python
"""
from flask import Flask
from flask import request
from flask import json
from flask import Response
from flask_restful import Resource
from flask_restful import Api
from api_restful_habilidades_flask import Habilidades
from api_restful_habilidades_flask import ListarHabilidades


# Criando uma lista para popular o sistema
devs = [
    {'id': 0,
     'nome': 'Rodrigo',
     'habilidades': ['Python', 'Flask']},
    {'id': 1,
     'nome': 'Pamela',
     'habilidades': ['Python', 'Django']}
]

app = Flask(__name__)
api = Api(app)

class Dev(Resource):
    """
    Classe responsável por lidar com operações CRUD
    para um desenvolvedor específico.

    Métodos:
    --------
    get(id):
        Retorna os detalhes de um desenvolvedor com o ID fornecido.
    
    post():
        Cria um novo desenvolvedor com base nos dados fornecidos.
    
    put(id):
        Atualiza os dados de um desenvolvedor existente com o ID fornecido.
    
    delete(id):
        Exclui o desenvolvedor com o ID fornecido.

    Exemplo de Uso:
    --------------
    # Criar uma instância da classe
    desenvolvedor = Dev()

    # Chamar os métodos CRUD conforme necessário
    detalhes_dev = desenvolvedor.get(0)
    resposta_post = desenvolvedor.post()
    resposta_put = desenvolvedor.put(1)
    resposta_delete = desenvolvedor.delete(2)

    """
    def get(self, id): # Com Restful não precisamos criar IFs e definir os métodos nos parametros
        """
        Retorna os detalhes de um desenvolvedor com o ID fornecido.

        Parameters:
        -----------
        id (int):
            O ID do desenvolvedor a ser recuperado.

        Returns:
        --------
        dict:
            Um dicionário contendo os detalhes do desenvolvedor.

        """
        try:
            response = devs[id]
            # Transforma a lista de habilidades em uma string separada por vírgula
            response['habilidades'] = ', '.join(response['habilidades'])
        except IndexError:
            response = {'status': 'erro',
                        'mensagem': f'Desenvolvedor de ID {id} não existe!'}
            print(f"Erro de execeção: {IndexError.__name__}")
        except Exception:
            response = {'status': f'erro {Exception.__name__}',
                        'mensagem': 'Procure o Admnistrador do sistema.'}
            print(f"O erro de exeção foi: {Exception.__name__}")
        return response
    def put(self, id):
        """
        Atualiza os dados de um desenvolvedor existente com o ID fornecido.

        Parameters:
        -----------
        id (int):
            O ID do desenvolvedor a ser atualizado.

        Returns:
        --------
        dict:
            Um dicionário contendo os dados atualizados do desenvolvedor.

        """
        response = json.loads(request.data)
        devs[id] = response
        return response
    def delete(self, id):
        """
        Exclui o desenvolvedor com o ID fornecido.

        Parameters:
        -----------
        id (int):
            O ID do desenvolvedor a ser excluído.

        Returns:
        --------
        dict:
            Um dicionário indicando o status da operação de exclusão.

        """
        if 0 <= id < len(devs):  # Certifica-se de que o índice é válido
            devs.pop(id)
            # Após a exclusão, reindexa os desenvolvedores
            for i, dev in enumerate(devs):
                dev['id'] = i
            return {'status': 'sucesso',
                            'mensagem': 'registro deletado'}
        return {'status': 'erro',
                            'mensagem': f'Desenvolvedor de ID {id} não existe!'}    

class ListarDevs(Resource):
    """
    Classe responsável por lidar com requisições GET para listar desenvolvedores.

    Métodos:
    --------
    get():
        Retorna uma resposta JSON com a lista de desenvolvedores, 
        formatando as habilidades como uma string.

    Exemplo de Uso:
    --------------
    # Criar uma instância da classe
        listar_devs = ListarDevs()

    # Chamar o método get para obter a lista formatada de desenvolvedores
        resposta = listar_devs.get()

    """
    def get(self):
        """
        Retorna uma resposta JSON com a lista de desenvolvedores, 
        formatando as habilidades e características como strings.

        Returns:
        --------
        Response:
            Uma resposta HTTP contendo a lista de desenvolvedores em formato JSON.

        Example:
        --------
        # Criar uma instância da classe
        listar_devs = ListarDevs()

        # Chamar o método get para obter a lista formatada de desenvolvedores
        resposta = listar_devs.get()

        """
        response_list = []

        # Itera sobre cada desenvolvedor na lista
        for dev in devs:
            # Formata as habilidades como uma string
            dev_info = {key: value
                        if key != 'habilidades'
                        else ', '.join(value)
                        for key, value in dev.items()
                        }
            # Usa json.dumps para lidar com a formatação JSON
            dev_str = json.dumps(dev_info, sort_keys=False, indent=2)
            response_list.append(dev_str)

        # Concatena as strings JSON separadas por vírgula
        response_str = ','.join(response_list)

        # Configura o Content-Type para application/json
        headers = {"Content-Type": "application/json"}

        # Retorna a resposta com o Content-Type configurado
        return Response(response_str, headers=headers)

    def post(self):
        """
        Cria um novo desenvolvedor com base nos dados fornecidos.

        Parameters:
        -----------
        None.

        Returns:
        --------
        dict:
            Um dicionário indicando o status da operação e uma mensagem associada.
            - 'status': Uma string indicando se a operação foi bem-sucedida.
            - 'mensagem': Uma mensagem descritiva sobre o resultado da operação.

        Example:
        --------
        # Criar uma instância da classe
        novo_dev = Dev()

        # Chamar o método post para adicionar um novo desenvolvedor
        resultado = novo_dev.post()

        """
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return {'status': 'Sucesso',
                'mensagem': 'Registro inserido!'}



api.add_resource(Dev, '/<int:id>/')
api.add_resource(ListarDevs, '/')
api.add_resource(ListarHabilidades, '/habilidades/')
api.add_resource(Habilidades, '/habilidades/<int:posicao>/')

if __name__ == "__main__":
    app.run(debug=True)
