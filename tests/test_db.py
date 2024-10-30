from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='mar', email='m#email.com', password='minhaSenha')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'm#email.com'))

    assert user.id == 1
    assert result.username == 'mar'
