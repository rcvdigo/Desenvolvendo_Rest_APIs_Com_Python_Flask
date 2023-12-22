"""
Módulo Habilidades Api Restful Devs
"""
from flask_restful import Resource
from flask import request, json

lst_habilidades = ["Java", "Python", "Kotlin"]

class ListarHabilidades(Resource):
    """
    Classe que representa a API para listar habilidades.

    Métodos:
    - get(): Retorna a lista de habilidades.
    - post(): Adiciona uma nova habilidade à lista.
    """

    def get(self):
        """
        Obtém a lista de habilidades.

        Returns:
            list: Lista de habilidades.
        """
        return lst_habilidades

    def post(self):
        """
        Adiciona uma nova habilidade à lista.

        Returns:
            dict: Dicionário contendo o status da operação e uma mensagem.
        """
        # Carrega os dados do request em formato JSON
        dados = json.loads(request.data)

        # Converte o dado para minúsculas para a verificação
        dado_minusculo = dados.lower()

        # Verifica se o dado já existe na lista em minúsculas
        if dado_minusculo in map(str.lower, lst_habilidades):
            return {'status': 'Falha',
                    'mensagem': 'Registro ja existe na lista!'}

        # Adiciona o dado em sua forma original na lista
        lst_habilidades.append(dados.title())

        return {'status': 'Sucesso',
                'mensagem': 'Registro inserido!'}


class Habilidades(Resource):
    """
    Classe que representa a API para operações individuais em habilidades.

    Métodos:
    - put(posicao): Atualiza uma habilidade na posição especificada.
    - delete(posicao): Remove uma habilidade na posição especificada.
    """

    def put(self, posicao):
        """
        Atualiza uma habilidade na posição especificada.

        Args:
            posicao (int): A posição da habilidade a ser atualizada.

        Returns:
            dict: Dicionário contendo o status da operação e uma mensagem.
        """
        response = json.loads(request.data)
        lst_habilidades[posicao] = response

        return {'status': 'sucesso',
                'mensagem': f'Registro na posicao {posicao} alterado com sucesso!!!'}

    def delete(self, posicao):
        """
        Remove uma habilidade na posição especificada.

        Args:
            posicao (int): A posição da habilidade a ser removida.

        Returns:
            dict: Dicionário contendo o status da operação e uma mensagem.
        """
        posicao = int(posicao)
        if 0 <= posicao < len(lst_habilidades):
            lst_habilidades.pop(posicao)
            return {'status': 'sucesso',
                    'mensagem': f'Registro na posicao {posicao} deletado com sucesso!'}
        else:
            return {'status': 'erro',
                    'mensagem': 'Posicao invalida'}
