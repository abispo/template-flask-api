from sqlalchemy import Integer

from database import db


class User(db.Model):
    __tablename__ = 'tb_users'

    _id = db.Column("id", Integer, primary_key=True, autoincrement=True)
    _name = db.Column("name", db.String(80), nullable=False)
    _email = db.Column("email", db.String(120))

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
