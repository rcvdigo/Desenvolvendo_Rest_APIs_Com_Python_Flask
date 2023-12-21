"""
Criando uma API com Flask
"""
from flask import Flask
from flask import jsonify
from flask import request
from flask import json


# Criando uma instância da aplicação Flask
my_app_flask = Flask(__name__)

# Criando uma lista para popular o sistema
tarefas = [
    {
        'id': 0,
        'responsavel': 'rafael',
        'tarefa': 'Desenvolver método GET',
        'status': 'concluído'
    },
    {
        'id': 1,
        'responsavel': 'Galleani',
        'tarefa': 'Desenvolver método POST',
        'status': 'pendente'
    },
]

# Criando uma rota e definindo uma função para minha rota
@my_app_flask.route("/<int:param_id>/", methods=['GET', 'PUT', 'DELETE'])
def index(param_id) -> str | None:
    """
    Rota para operações CRUD em tarefas específicas.

    Args:
        param_id (int): O ID da tarefa.

    Returns:
        str: Detalhes da tarefa.
    """
    if request.method == 'GET':
        try:
            response = tarefas[param_id]
        except IndexError:
            response = {'status': 'erro',
                        'mensagem': f'Tarefa de ID {param_id} não existe!'}
        # except Exception as e:
        #     response = {'status': f'erro {type(e).__name__}',
        #                 'mensagem': 'Procure o Administrador do sistema.'}
        return (
            f'ID: {response["id"]}<br/>'
            f'Responsavel: {response["responsavel"].title()}<br/>'
            f'Tarefa: {response["tarefa"]}<br/>'
            f'Status: {response["status"].title()}'
        )
    if request.method == 'PUT':
        try:
            dados = json.loads(request.data)
            tarefas[param_id]['status'] = dados['status']
        except IndexError:
            dados = {'status': 'erro',
                     'mensagem': f'Tarefa de ID {param_id} não existe!'}
        # except Exception as e:
        #     response = {'status': f'erro {type(e).__name__}',
        #                 'mensagem': 'Procure o Administrador do sistema.'}
        return jsonify(tarefas[param_id])
    if request.method == 'DELETE':
        if 0 <= param_id < len(tarefas):  # Certifica-se de que o índice é válido
            tarefas.pop(param_id)
            # Após a exclusão, reindexa as tarefas
            for i, tasks in enumerate(tarefas):
                tasks['id'] = i
            return jsonify({'status': 'sucesso',
                            'mensagem': 'registro deletado'})
        # Se o id passado no parametro não existir
        return jsonify({'status': 'erro',
                        'mensagem': f'Desenvolvedor de ID {param_id} não existe!'})
    return None


# Listando todas tarefas e incluir um nova tarefa
@my_app_flask.route('/', methods=['POST', 'GET'])
def listar_tarefas() -> str | None:
    """
    Rota para listar todas as tarefas ou inserir uma nova tarefa.

    Returns:
        str: Lista de todas as tarefas ou mensagem de sucesso após a inserção.
    """
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify({'status': 'Sucesso',
                        'mensagem': 'Registro Inserido!'})
    if request.method == 'GET':
        todas_tarefas = '<br/><br/>'.join([
            f'ID: {dados["id"]}<br/>'
            f'Responsavel: {dados["responsavel"].title()}<br/>'
            f'Tarefa: {dados["tarefa"].title()}<br/>'
            f'Status: {dados["status"].title()}'
            for dados in tarefas
        ])
        return todas_tarefas
    return None


# Iniciando o microframework flask
if __name__ == "__main__":
    my_app_flask.run(debug=True)
