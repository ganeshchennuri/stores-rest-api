from db import db

class UserModel(db.Model):  #Extending db.Model creates mapping between Database and class objects, we can insert, update delete using objects
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200))

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
        
    @classmethod
    def find_by_userid(cls,_id): #Querying table with userid filter
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)    #Adding users to Database
        db.session.commit()