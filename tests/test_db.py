from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='renan', email='test@test.com', password='secret'
        )

        # Adiciona um novo registro a sessão (estado transitivo/intermediario)
        session.add(new_user)
        # Registra de fato no banco de dados (etapa final)
        session.commit()

        # Retorna o resultado da busca em um objeto python
        user = session.scalar(select(User).where(User.username == 'renan'))

        assert asdict(user) == {
            'id': 1,
            'username': 'renan',
            'email': 'test@test.com',
            'password': 'secret',
            'created_at': time,
        }
