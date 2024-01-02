"""
api_atividades (arquivo: app.py)
"""
from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from api_sqlalchemy_exercicio_models import Programador
from api_sqlalchemy_exercicio_models import Usuarios
from api_sqlalchemy_exercicio_models import Habilidade
from api_sqlalchemy_exercicio_models import ProgramadorHasHabilidade


auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# Usando authenticação em HARDCODE
# USUARIOS = {
#     'rcvdigo':'1233',
#     'ptcs': '321'
# }


# @auth.verify_password
# def verificacao(login, senha):
#     """
#     Verifica a autenticação do usuário.

#     Args:
#         login (str): Nome de usuário.
#         senha (str): Senha do usuário.

#     Returns:
#         bool: True se a autenticação for bem-sucedida, False caso contrário.
#     """
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha

# Usando authenticação no banco de dados
@auth.verify_password
def verificacao(login, senha):
    """
    Verifica a autenticação do usuário.

    Args:
        login (str): Nome de usuário.
        senha (str): Senha do usuário.

    Returns:
        bool: True se a autenticação for bem-sucedida, False caso contrário.
    """
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class ProgramadorRestful(Resource):
    """
    Classe que representa um recurso RESTful para manipulação de programadores.
    """
    @auth.login_required
    def get(self, nome):
        """
        Obtém detalhes de um programador pelo nome.

        Args:
            nome (str): Nome do programador.

        Returns:
            dict: Dicionário contendo detalhes do programador.
        """
        programador = Programador.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': programador.nome,
                'idade': programador.idade,
                'id': programador.id
            }
            return response
        except AttributeError:
            error_msg = f"O atributo informado [{nome}] nao existe cadastrado no banco!!!"
            response = {
                'status':'error',
                'tipo':AttributeError.__name__,
                'msg':error_msg
            }
            return response

    def put(self, nome):
        """
        Atualiza informações de um programador pelo nome.

        Args:
            nome (str): Nome do programador.

        Returns:
            dict: Dicionário contendo informações atualizadas do programador.
        """
        programador = Programador.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            programador.nome = dados['nome']
        if 'idade' in dados:
            programador.idade = dados['idade']
        programador.save()
        response = {
            'id':programador.id,
            'nome':programador.nome,
            'idade':programador.idade
        }
        return response

    def delete(self, nome):
        """
        Exclui um programador pelo nome.

        Args:
            nome (str): Nome do programador.

        Returns:
            dict: Dicionário indicando o status da exclusão.
        """
        programador = Programador.query.filter_by(nome=nome).first()
        if programador:
            # Excluir a relação em vez do programador diretamente
            # programador.delete_relations()
            programador.delete()
            error_msg = f"Programador {nome} excluído com sucesso"
            response = {
                'status': 'sucesso',
                'mensagem': error_msg
            }
            return response

        error_msg = f"Programador {nome} não encontrado"
        response = {
            'status': 'erro',
            'mensagem': error_msg
        }
        return response

api.add_resource(ProgramadorRestful, '/programador/<string:nome>/')

class ListarProgamadores(Resource):
    """
    Classe que representa um recurso RESTful para listar programadores.
    """
    def get(self):
        """
        Lista todos os programadores.

        Returns:
            list: Lista de dicionários contendo informações de programadores.
        """
        programador = Programador.query.all()
        response = [{'id':devs.id, 'nome':devs.nome, 'idade':devs.idade} for devs in programador]
        return response

    def post(self):
        """
        Adiciona um novo programador.

        Returns:
            dict: Dicionário contendo informações do novo programador.
        """
        dados = request.json
        programador = Programador(nome=dados["nome"], idade=dados["idade"])
        programador.save()
        response = {
            'id':programador.id,
            'nome':programador.nome,
            'idade':programador.idade
        }
        return response

api.add_resource(ListarProgamadores, '/programador/')

class ListarHabilidades(Resource):
    """
    Classe que representa um recurso RESTful para listar habilidades.
    """
    def get(self):
        """
        Lista todas as habilidades.

        Returns:
            list: Lista de dicionários contendo informações de habilidades.
        """
        habilidades = Habilidade.query.all()
        response = [
            {
                'id': habilidade.id,
                'nome': habilidade.nome
            } for habilidade in habilidades
        ]
        return response

    def post(self):
        """
        Adiciona uma nova habilidade.

        Returns:
            dict: Dicionário contendo informações da nova habilidade.
        """
        dados = request.json
        habilidade = Habilidade(nome=dados["nome"])
        habilidade.save()
        response = {
            'id':habilidade.id,
            'nome':habilidade.nome
        }
        return response

api.add_resource(ListarHabilidades, '/habilidade/')

class ListarProgramadorHasHabilidade(Resource):
    """
    Classe que representa um recurso RESTful para listar relações entre programadores e habilidades.
    """
    def get(self):
        """
        Lista todas as relações entre programadores e habilidades.

        Returns:
            list: Lista de dicionários contendo informações das relações.
        """
        ph = ProgramadorHasHabilidade.query.all()
        response = [
            {'id':phs.id,
             'programador':phs.programador_rlt.nome, 
             'habilidade':phs.habilidade_rlt.nome
            } for phs in ph
        ]
        return response

    def post(self):
        """
        Adiciona uma nova relação entre programador e habilidade.

        Returns:
            dict: Dicionário indicando o status da adição da nova relação.
        """
        dados = request.json
        print(dados)
        programador = Programador.query.filter_by(nome=dados['programador']).first()
        habilidade = Habilidade.query.filter_by(nome=dados['habilidade']).first()
        programador_nova_habilidade = ProgramadorHasHabilidade(
            id_programador=programador.id,
            id_habilidade=habilidade.id
        )
        programador_nova_habilidade.save()
        response = {
            'status':'sucesso',
            'msg':f'nova habilidade adicionada ao programador {programador.nome}',
            'programador':programador.nome,
            'habilidade':habilidade.nome
        }
        return response


api.add_resource(ListarProgramadorHasHabilidade, '/ph/')


class ListarProgramadorHasHabilidadeNome(Resource):
    """
    Classe que representa um recurso RESTful para listar 
    relações entre programadores e habilidades filtrando pelo
    nome do programador.
    """
    def get(self, nome):
        """
        Lista todas as relações entre programador e habilidade pelo nome do programador.

        Args:
            nome (str): Nome do programador.

        Returns:
            list: Lista de dicionários contendo informações das relações.
        """
        programador = Programador.query.filter_by(nome=nome).first()
        ph = ProgramadorHasHabilidade.query.filter_by(id_programador=programador.id).all()
        response = [
            {
                'id':phs.id,
                'programador':phs.programador_rlt.nome,
                'habilidade':phs.habilidade_rlt.nome
            } for phs in ph
        ]
        return response

api.add_resource(ListarProgramadorHasHabilidadeNome, '/ph/<string:nome>/')

if __name__ == '__main__':
    app.run(debug=True)
