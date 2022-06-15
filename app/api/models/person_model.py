from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# solves circular import...
class PersonModel(db.Model):

    __tablename__ = 'persons'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    age = db.Column(db.Integer(), unique=False, nullable=False)
    gender = db.Column(db.String(6), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    # def __init__(self, name, age, gender, email):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender
    #     self.email = email

    def find_by_email(self, email: str) -> "PersonModel":
        return self.query.filter_by(email=email).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f"<Person {self.id}: name={self.name}, email={self.email}>"