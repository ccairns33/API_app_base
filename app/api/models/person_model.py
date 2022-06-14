from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    age = db.Column(db.Integer(), unique=False, nullable=False)
    gender = db.Column(db.String(6), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Person {self.id}: name={self.name}, email={self.email}>"