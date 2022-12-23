import db
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from sqlalchemy import Column, String, Float, Integer, Boolean


class User(db.Base):

    __tablename__ = 'producto'
    __table_args  = {'sqlite_autoincrement':True}


    id_user = Column(Integer,primary_key = True)
    name_user = Column(String(100), nullable=False)
    surnames_user = Column(String(150), nullable=False)
    age_user = Column(Integer,nullable=False)
    mail_user = Column(String(150),nullable=False)
    username = Column(String(20), nullable=False)
    password_user = Column(String(8),nullable=False)
    photo_user = Column(String, nullable=False)


    def __init__(self, name_user, surnames_user, age_user, mail_user, username, password_user, photo_user):
        self.name_user = name_user
        self.surnames_user = surnames_user
        self.age_user = age_user
        self.mail_user = mail_user
        self.username = username
        self.password_user = self.__create_password(password_user)
        self.photo_user = photo_user


    def __create_password(self,password):
        return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_user, password)

    def __str__(self):
        return f'''
        Name: {self.name_user}
        Surnames: {self.surnames_user}
        Age: {self.age_user}
        Username: {self.username}
        Mail: {self.mail_user}
        Photo: {self.photo_user}'''