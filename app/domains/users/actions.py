from typing import Dict

from app.domains.users.models import User
from database.repository import save


def create(data: Dict[str, str]):
    return save(User(name=data["name"], email=data["email"]))


def get():
    return User.query.all()


def get_by_id(id: int):
    return User.query.get(id)


def update(id: int, data: Dict[str, str]):
    user = get_by_id(id)
    user.name = data.get("name")
    user.email = data.get("email")

    return save(user)
