from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base:
    def to_dict(self):
        dic = self.__dict__
        dic.pop("_sa_instance_state")
        return dic


class StudentModel(db.Model, Base):
    __tablename__ = 'students'

    ID = db.Column(db.Integer(), primary_key=True)
    NAME = db.Column(db.String())
    AGE = db.Column(db.Integer())
    GENDER = db.Column(db.String())

    def __init__(self, name, age, gender):
        self.NAME = name
        self.AGE = age
        self.GENDER = gender

    def __repr__(self):
        return f"{self.NAME}:{self.ID}"
