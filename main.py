from flask import redirect, render_template, url_for, request, Flask, send_file, flash
from utils import create_user
import models
from models import User
import db
from werkzeug.utils import secure_filename
from datetime import datetime
from flask.globals import session


app = Flask(__name__)
app.secret_key = "adbcdefg23533@!#-$3$!EDFw"

# La ruta raiz
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/logeo",methods=["POST","GET"])
def logeo():
    if(request.method == "POST"):
        user = request.form["usuario"]
        contrasenia = request.form["password"]

        consulta_usuario = db.session.query(User).filter(User.username == user).first()

        if(consulta_usuario is not None and consulta_usuario.verify_password(contrasenia)):
            session['usuario'] = user
            session["rol"] = "usuario"
            return render_template("session.html")
        else:
            flash("Datos incorrectos")
            return redirect(url_for('home'))

    elif(request.method == "GET"):
        return redirect(url_for('home'))


@app.route("/close-session")
def close_session():
    session.clear()
    return redirect(url_for('home'))

if(__name__ == '__main__'):
    db.Base.metadata.create_all(db.engine)

    app.run(debug=True)