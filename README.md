Objetivos
* Criar uma base teórica sobre desenvolvimento web
    - A WEB:
        Básicamente é uma coisa que funciona em uma rede (um ou mais dispositivos que se comunicam)
        Local (LAN): como em sua casa ou em uma empresa
        Longa sistância (WAN): como diversos roteadores interconectados
        Mundial: como a própria internet
    - Client-Servidor
        O garçon serve o cliente
        garçon!! me ver uma lasanha? Sim. Claro!!
    - Uvicorn
        servidor de aplicação (ASGI)
        fastapi seria o prato e uvicorn o garçon
    - A rede local
        loopback: o servidor e o client então na mesma maquina
    - Servindo na rede local (LAN)
        saindo do loopback, podemos abrir o servidor do uvicorn para rede local:
            fastapi dev fast_zero/app.py --host 0.0.0.0
    - URL: http://127.0.0.1:8000
        protocolo: http://
        endereço: 127.0.0.1
        porta: :8000
        localizador uniforme de recurso
* Apresentar o protocolo HTTP
    - Hipertext Transfer Protocol
    - linguagem de comunicação
    - formaliza a forma de comunicação entre cliente e servidor
    - tanto requisição quanto respostas são referidas como mensagem
        GET / HTTP/1.1
        Accept: */*
        Accept-Encoding: gzip, deflate
        Connection: keep-alive
        Host: 127.0.0.1:8000
        User-Agent: HTTPie/3.2.2
    
        HTTP/1.1 200 OK
        content-length: 24
        content-type: application/json
        date: Fri, 19 Jan 2024 04:05:50 GMT
        server: uvicorn
        {
            "message": "Olá mundo"
        }
    - verbos:
        GET - obtem dados
        POST - envia dados
        PUT - altera dados
        DELETE - remove dados
    - códigos de resposta:
        2xx - sucesso
            200 - OK
            201 - Create
        3xx - redirecionamento
        4xx - erro no cliente
            404 - Not Found
            422 - Unprocessable Entity
        5xx - erro no servidor
            500 - Internal Server Error
    - FastAPI e códigos de resposta:
        @app.get('/', status_code=HTTPStatus.OK)
        def read_root():
            return {'message': 'Olá Mundo!'}    
* Introduzir os conceitos de APIs JSON
    - Application Programming Interfaces
    - Javascript Object Notation
* Apresentar o OpenAPI
* Introduzir os schemas usando Pydantic
    - No universon de APIs e contratos de dados, especialmente a trabalhar com Python, o Pydantic
      se destaca como uma ferramenta poderosa e versátil. Além de embutida no FastAPI.
    - A ideia dele é criar uma camada de documentação, via OpenAPI, e de fazer a validação dos
      modelos de entrada e saída da nossa API.
    
    from pydantic import BaseModel

    class Message(BaseModel):
        message: str

Operações com dados
Associações com HTTP
 - Create - POST
 - Read - GET
 - Update - PUT
 - Delete - DELETE

SQLAlchemy
 - ORM. Na verdade ele tem um ORM.
        permite trabalhar com SQL, ou any bancos sql.
        Mapeamento Objeto-Relacional.
        vai mapear o objeto no relacionamento.
        abstração do banco de dados. Em outras palavras tenho a possibilidade de mudar de banco sem quebrar a lógica do negócio.
 - The Twelve Factors (boas praticas)
        excluir variaveis de dentro do código
 - Migrations
        é preciso criar uma evolução no banco de dados
        o banco de dados acompanha as alterações do código
        reverter alterações no schema do banco
* Integrando Banco de Dados (SQLAlchemy) ao FastAPI
 - ORM. a peça principal dessa integração será p ORM
 - Padrões da sessão
    Repositório
    Unidade de Trabalho: chamada unica ao banco para economizar recurso
    Mapeamento de Identidade