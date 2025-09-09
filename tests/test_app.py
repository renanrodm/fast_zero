from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    Teste em 3 etapas (AAA)
    - #Arrange: Arranjo/Organizar
    - #Act: Executa a coisa (o SUI)
    - #Assert: Garanta que A é A
    """
    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá, Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_hello_world_deve_retornar_ola_mundo_html(client):
    response = client.get('/helloworld')

    assert response.status_code == HTTPStatus.OK
    assert response.text == '<html><h1>Olá, Mundo!</h1></html>'


def test_create_user(client):
    # Enviamos com o User, schema de entrada
    response = client.post(
        '/users/',
        json={
            'username': 'Renan',
            'password': '12345',
            'email': 'renan@email.com',
        },
    )

    # Validar o UserPublic, schema de saída.
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Renan',
        'email': 'renan@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Renan',
                'email': 'renan@email.com',
                'id': 1,
            }
        ]
    }
    # [MÁ PRÁTICA]: Esse teste depende do teste de cima para validar os dados.
    # O motivo disso é por não termos o banco dados real implementado. Ainda...


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Renan',
            'password': '12345',
            'email': 'renan@email.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'Renan',
        'email': 'renan@email.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Renan',
            'password': '12345',
            'email': 'renan@email.com',
            'id': 999,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
