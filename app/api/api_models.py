# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db


# Data model is an abstract representaion of the database
# Schema describes the layout of the data IN the database:
# what kinda of fields are present and how they are organized
# contains a definition of what data our application deals with

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )


# Define a User model
class User(Base):

    __tablename__ = "auth_user"

    # User Name
    name = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorisation Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"
