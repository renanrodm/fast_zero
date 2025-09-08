from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Teste em 3 etapas (AAA)
    - #Arrange: Arranjo/Organizar
    - #Act: Executa a coisa (o SUI)
    - #Assert: Garanta que A é A
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá, Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_hello_world_deve_retornar_ola_mundo_html():
    client = TestClient(app)

    response = client.get('/helloworld')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<html><h1>Olá, Mundo!</h1></html>'
