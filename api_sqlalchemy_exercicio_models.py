"""
api_atividades (Arquivo: models.py)
"""
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# Criando o banco de dados
engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
# Final da criação do banco de dados

class Usuarios(Base):
    """
    Classe que representa a tabela 'usuarios' no banco de dados.

    Atributos:
        id (int): Identificador único do usuário.
        login (str): Nome de usuário.
        senha (str): Senha do usuário.
    """
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        """
        Retorna uma representação textual do objeto Usuario.

        Returns:
            str: String representando o objeto Usuario.
        """
        return f'Usuario: {self.login}'

    def save(self):
        """
        Salva o objeto Usuario no banco de dados.
        """
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """
        Exclui o objeto Usuario do banco de dados.
        """
        db_session.delete(self)
        db_session.commit()


class Programador(Base):
    """
    Classe que representa a tabela 'programador' no banco de dados.

    Atributos:
        id (int): Identificador único do programador.
        nome (str): Nome do programador.
        idade (int): Idade do programador.
        e_mail (str): Endereço de e-mail do programador.
        rlt_programador (Relationship): Relacionamento com a tabela 'ProgramadorHasHabilidade'.
    """
    __tablename__ = 'programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    e_mail = Column(String(40))

    rlt_programador = relationship(
        'ProgramadorHasHabilidade',
        back_populates='programador_rlt'
    )

    def __repr__(self):
        """
        Representação textual do objeto Programador.

        Returns:
            str: String representando o objeto Programador.
        """
        return (
            f'Nome da Tabela: {self.__tablename__}\n'
            f'Id: {self.id}\n'
            f'Nome: {self.nome}\n'
            f'Idade: {self.idade}\n'
            f'E-mail: {self.e_mail}'
        )

    def save(self):
        """
        Salva o objeto Programador no banco de dados.
        """
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """
        Exclui o objeto Programador do banco de dados.
        """
        db_session.delete(self)
        db_session.commit()

    def delete_relations(self):
        """
        Exclui o objeto do banco de dados.
        """
        for relacao in self.rlt_programador:
            db_session.delete(relacao)
        db_session.commit()

class Habilidade(Base):
    """
    Classe que representa a tabela 'habilidade' no banco de dados.

    Atributos:
        id (int): Identificador único da habilidade.
        nome (str): Nome da habilidade.
        rlt_habilidade (Relationship): Relacionamento com a tabela 'ProgramadorHasHabilidade'.
    """
    __tablename__ = 'habilidade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80), index=True)

    rlt_habilidade = relationship(
        'ProgramadorHasHabilidade',
        back_populates='habilidade_rlt'
    )

    def __repr__(self):
        """
        Representação textual do objeto Habilidade.

        Returns:
            str: String representando o objeto Habilidade.
        """
        return (
            f'Nome da Tabela: {self.__tablename__}\n'
            f'Id: {self.id}\n'
            f'Nome: {self.nome}'
        )

    def save(self):
        """
        Salva o objeto Habilidade no banco de dados.
        """
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """
        Exclui o objeto Habilidade do banco de dados.
        """
        db_session.delete(self)
        db_session.commit()

class ProgramadorHasHabilidade(Base):
    """
    Classe que representa a tabela 'programadorhashabilidade' no banco de dados.

    Atributos:
        id (int): Identificador único da relação.
        id_programador (int): Identificador único do programador associado.
        id_habilidade (int): Identificador único da habilidade associada.
        programador_rlt (Relationship): Relacionamento com a tabela 'Programador'.
        habilidade_rlt (Relationship): Relacionamento com a tabela 'Habilidade'.
    """
    __tablename__ = 'programadorhashabilidade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_programador = Column(Integer, ForeignKey('programador.id'), nullable=False)
    id_habilidade = Column(Integer, ForeignKey('habilidade.id'), nullable=False)

    programador_rlt = relationship(
        'Programador',
        back_populates='rlt_programador'
    )

    habilidade_rlt = relationship(
        'Habilidade',
        back_populates='rlt_habilidade'
    )

    def __repr__(self):
        """
        Representação textual do objeto ProgramadorHasHabilidade.

        Returns:
            str: String representando o objeto ProgramadorHasHabilidade.
        """
        return (
            f'Nome da Tabela: {self.__tablename__}\n'
            f'Id: {self.id}\n'
            f'Id Programador: {self.id_programador}\n'
            f'Id Habilidade: {self.id_habilidade}'
        )

    def save(self):
        """
        Salva o objeto ProgramadorHasHabilidade no banco de dados.
        """
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """
        Exclui o objeto ProgramadorHasHabilidade do banco de dados.
        """
        db_session.delete(self)
        db_session.commit()

def init_db():
    """
    Inicializa o banco de dados criando as tabelas.
    """
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
