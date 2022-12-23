from models import User
import db

def create_user():
    a = User(name_user="admin",surnames_user="admin_admin",age_user=23,mail_user='admin@gmail.com',username="admin",password_user='0',
             photo_user="hola.jpg")
    db.session.add(a)
    db.session.commit()
    return print("Se ha creado el usuario")