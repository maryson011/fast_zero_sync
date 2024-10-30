from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <head>
                <title> Nosso olá mundo!</title>
            </head>
            <body>
                <h1>Olá Mundo</h1>
                <h2>minha primeira página expondo o local na LAN</h2>
            </body>
        </html>
    """
