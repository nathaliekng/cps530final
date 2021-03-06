from app import db

class User(db.Model):
    #Create Database columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)


    def _repr_(self):
        return '<User{}>'.format(self.username)