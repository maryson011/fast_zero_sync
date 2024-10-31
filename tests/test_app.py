from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'teste',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # validar o UserPublic
    assert response.json() == {
        'username': 'teste',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client, user):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'teste2',
            'email': 'test@test.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'teste2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'password': '123',
            'username': 'teste3',
            'email': 'test@test.com',
            'id': 2,
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted'}


def test_delete_not_found(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
