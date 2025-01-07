from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email

        }

class Planet(db.Model):
    __tablename__ = 'Planet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(120), unique=True)
    population = db.Column(db.Integer, primary_key=False)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "population": self.population

        }
    
class People(db.Model):
    __tablename__ = 'People'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(120), unique=True)
    race = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "race": self.race

        }
