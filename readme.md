# O que é uma API?

- É um conjunto de rotinas para acesso a um aplicativo/software/plataforma baseado em Web.
- Acrônimo de __Application Programming Interface - Interface de programação de aplicativos__.
- APIs são importantes quando se tem a inteção de realizar integrações com outros serviços.
- Com as APIs a comunicação de software fica transparente ao usuário.
- APIs podem ser locais, baseada em web e baseada em programas.

# O que é REST?

- É um modelo a ser utilizado para projetar arquiteturas de software baseado em comunicação via rede.
- Acrônimo de **Representational State Transfer (Transferência de Estado Representacional)**.
- Foi definido por Roy Fielding em sua tese de doutorado (PhD) na UC Irvine no ano 2000.
- REST projeta a idéia de que todo recurso deveria responder aos mesmos métodos.   

# O que é REST API?

- É uma API desenvolvida utilizando os princípios da arquitetura REST.
- Um REST API é utilizado na comunicação/integração entre software através de serviços WEB.
- Um REST API é consumido através de requisições HTTP.
- REST APIs são geralmente representadas em seus formatos por JSON e XML. Também são usados páginas HTML, PDF e arquivos de imagens.
- Ao implementar um REST API, cada método deve ser responsável por um tipo diferente de ação. Exemplo: Consulta, Alteração, Inclusão e Exclusão ou (CRUD).

# Métodos do protocolo HTTP

- GET: Método que solicita algum recurso ou objeto do servidor por meio da URI.
- POST: Método usado para envio de arquivo/dados ou formulário HTML para o servidor.
- PUT: Aceitar criar ou modificar um objeto do servidor.
- DELETE: Informa por meio da URI o objeto a ser deletado.


PUT = CREATE <br/>
GET = READ <br/>
POST = UPDATE <br/>
DELETE = DELETE <br/>


# URL x URN vs URI?

- URL: Uniform Resource Locator - Localizador de Recursos Universal.
    - Host que será acessado. Exemplo globallabs.academy.
- URN: Uniform Resource Name - Nome do Recurso Universal.
    - É o recurso que será identificado. Exemplo: category/blog.
- URI: Uniform Resource Identifier - Identificador de Recursos Universal.
    - É o identificador do recurso, podendo ser uma imagem, um arquivo ou uma página. Exemplo: https://globallabs.academy/category/blog/.
- URI une Protocol(https://), URL(globallabs.academy) e URN(/category/blog/).


# XML - Extensible Markup Language

- É uma linguagem de marcação.
- Utilizada para compartilhamento de informações através de requisições HTTP.


# JSON - JavaScript Object Notation

- É um formato de troca de dados entre sistemas independente da linguagem utilizada derivada do JavaScript.
- Muitas linguagens possuem suporte ao JSON.


# Flask

- É um microFrameWork para Python utilizado para desenvolvimento de aplicações WEB.
- É chamado de microFrameWork porque mantém um núcleo simples, mas é estendível.
- Flask não possuí camada de abstração para banco de dados, validação de formulários entre outros, mas é possível estender com outras bibliotecas.
- Por ser leve e simples de usar, Flask é um dos frameworks Python mais usados para desenvolvimento de APIs.

# Agenda

- PIP.
- Instalação do Flask.
- Criando um ambiente virtual (VirtualEnv).
- Primeira aplicação Flask.
- Entendendo os decoladores.
- Postman para realizar requisições HTTP.

# O que utilizaremos?

- Python 3.7.
- Pycharm Community.
- Flask.
- Postman.

# PIP

- Sistema de gerenciamento de pacotes.
- Utilizado para instalar e gerenciar pacotes/bibliotecas em Python.
- Já vem empacotado com Python desde a versão 3.4.<br/>


> <span>></span> <span style="color:yellow">pip</span> <span style="color:white">install Flask</span>

# Virtualenv

- Ferramenta para criar ambientes Python isolados.
- Vem integrado com Python desde a versão 3.3.
- Extremamente útil para se trabalhar com projetos que utilizam bibliotecas com versões diferentes.

> <span style="color:yellow"> python </span><span style="color:gray"> -m </span> <span style="color:white"> venv .\\.virtualenvs\minha_virtualenv </span><br/>
> <span style="color:yellow"> .\\.virtualenvs\minha_virtualenv\Scripts\activate </span><br/>
> <span style="color:green"> (minha_virtualenv) </span> <span style="color:yellow"> pip </span> <span style="color:white"> install Flask </span><br/>


```python
"""
Meu primeiro app com Flask
"""
from flask import Flask


# Herdando a biblioteca Flask na variável my_app_flask
my_app_flask = Flask(__name__)
# Definindo a rota inicial index.html
@my_app_flask.route("/")
# Definindo a função da index.html

def index():
    """
    Criando a página index.html
    """
    return "Hello World"

if __name__ == "__main__":
    my_app_flask.run()
```
