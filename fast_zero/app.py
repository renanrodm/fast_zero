from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(title='Fast Zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get('/helloworld', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_world():
    return """<html><h1>Olá, Mundo!</h1></html>"""
