"""
api_atividades (Arquivo: utils.py)
"""
from api_sqlalchemy_exercicio_models import Programador
from api_sqlalchemy_exercicio_models import Habilidade
from api_sqlalchemy_exercicio_models import ProgramadorHasHabilidade
from api_sqlalchemy_exercicio_models import Usuarios


def insere():
    """
    Insere dados de exemplo nas tabelas.
    """
    # Criando programadores
    programador1 = Programador(
        nome='Vera', idade=29, e_mail='rcvdigo@gmail.com')
    programador2 = Programador(
        nome='Carlos', idade=25, e_mail='carlos@gmail.com')

    # Criando habilidades
    habilidade1 = Habilidade(nome='Python')
    habilidade2 = Habilidade(nome='SQL')

    # Salvando no banco de dados
    programador1.save()
    programador2.save()
    habilidade1.save()
    habilidade2.save()

    # Associando habilidades aos programadores usando os IDs
    programador1_habilidade1 = ProgramadorHasHabilidade(
        id_programador=programador1.id,
        id_habilidade=habilidade1.id
    )

    programador1_habilidade2 = ProgramadorHasHabilidade(
        id_programador=programador1.id,
        id_habilidade=habilidade2.id
    )

    programador2_habilidade1 = ProgramadorHasHabilidade(
        id_programador=programador2.id,
        id_habilidade=habilidade1.id
    )

    # Salvando no banco de dados
    programador1_habilidade1.save()
    programador1_habilidade2.save()
    programador2_habilidade1.save()


def consulta_programador(nome_pessoa=None):
    """
    Consulta programadores no banco de dados.

    Args:
        nome_pessoa (str): Nome do programador a ser consultado.

    Returns:
        None: Se nome_pessoa não for especificado.
        dict: Dicionário contendo detalhes do programador consultado.
    """
    if nome_pessoa is None:
        programador = Programador.query.all()
        for programadores in programador:
            print(programadores, end='\n\n')
    else:
        programador = Programador.query.filter_by(nome=nome_pessoa).first()
        print(programador)


def consulta_habilidade(nome_habilidade=None):
    """
    Consulta habilidades no banco de dados.

    Args:
        nome_habilidade (str): Nome da habilidade a ser consultada.

    Returns:
        None: Se nome_habilidade não for especificado.
        dict: Dicionário contendo detalhes da habilidade consultada.
    """
    if nome_habilidade is None:
        habilidade = Habilidade.query.all()
        for habilidades in habilidade:
            print(habilidades, end='\n\n')
    else:
        habilidade = Habilidade.query.filter_by(nome=nome_habilidade).first()
        print(habilidade)


def consulta_p_h(id_ph=None):
    """
    Consulta relações entre programadores e habilidades no banco de dados.

    Args:
        id_ph (int): ID da relação a ser consultada.

    Returns:
        None: Se id_ph não for especificado.
        dict: Dicionário contendo detalhes da relação consultada.
    """
    if id_ph is None:
        programador_has_habilidade = ProgramadorHasHabilidade.query.all()
        for data in programador_has_habilidade:
            print(data, end='\n\n')
    else:
        programador_has_habilidade = ProgramadorHasHabilidade.query.filter_by(
            nome=id_ph).first()
        print(programador_has_habilidade)

def alterar_nome_pessoa(nome_atualizado=None, nome_anterior=None):
    """
    Altera o nome de uma pessoa no banco de dados.

    Args:
        nome_atualizado (str): Novo nome a ser atribuído.
        nome_anterior (str): Nome atual da pessoa a ser alterado.

    Returns:
        None
    """
    if nome_anterior is None:
        print("Necessário informar o nome_anterior para poder realizar a modificação!!!")
    else:
        if nome_atualizado is None:
            print("Nenhum registro foi alterado por falta de parâmetros")
        else:
            pessoa = Programador.query.filter_by(nome=nome_anterior).first()  # Filtrar pessoa
            if pessoa:
                pessoa.nome = nome_atualizado  # Atualizar nome
                pessoa.save()  # Confirmar alteração no banco de dados
                print(f"O nome antigo '{nome_anterior}' foi alterado para '{nome_atualizado}'")
            else:
                print(f"Nenhum programador encontrado com o nome '{nome_anterior}'")

def deleta_pessoa(person_id=None, nome=None):
    """
    Deleta uma pessoa do banco de dados.

    Args:
        person_id (int): ID da pessoa a ser deletada.
        nome (str): Nome da pessoa a ser deletada.

    Returns:
        None
    """
    if person_id is None and nome is None:
        print("Necessário informar o id ou nome!!!")
    elif person_id is not None:
        pessoa = Programador.query.filter_by(id=person_id).first()  # Filtrar pessoa pelo ID
        if pessoa:
            print(f"O registro: {pessoa} \nfoi deletado com sucesso!!!")
            pessoa.delete()  # Excluir a pessoa do banco de dados
        else:
            print(f"Nenhum programador encontrado com o ID '{person_id}'")
    elif nome is not None:
        pessoa = Programador.query.filter_by(nome=nome).first()  # Filtrar pessoa pelo nome
        if pessoa:
            print(f"O registro: {pessoa} \nfoi deletado com sucesso!!!")
            pessoa.delete()  # Excluir a pessoa do banco de dados
        else:
            print(f"Nenhum programador encontrado com o nome '{nome}'")


def insere_usuario(login, senha):
    """
    Insere um novo usuário no banco de dados.

    Args:
        login (str): Nome de usuário.
        senha (str): Senha do usuário.
    """
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consultar_usuarios():
    """
    Consulta e imprime todos os usuários cadastrados no banco de dados.
    """
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere()
    # print("-="*13)
    # consulta() # Todos os registros
    print("-="*13)
    # insere_usuario(login='rcvdigo', senha='1234')
    # insere_usuario(login='pamtheo', senha='4321')
    # consultar_usuarios()
    # consulta_programador()  # Filtrando o registro
    # consulta_habilidade()  # Filtrando o registro
    # consulta_p_h()  # Filtrando o registro
    print("-="*13)
    # alterar_nome_pessoa(nome_atualizado=None, nome_anterior="Teste")
    # print("-="*13)
    # deleta_pessoa()
