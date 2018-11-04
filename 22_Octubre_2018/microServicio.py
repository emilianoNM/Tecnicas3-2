#FLASK_APP=microServicio.py flask run

from flask import * 

app = Flask(__name__)

@app.route("/")
def hello():
    return "<form method='post' action='respuesta'> <p>Texto dentro del formulario</p>  <p><input type='text' name='username' /></p> <input type='submit' value='Enviar' /> </form>"

@app.route("/respuesta", methods=['GET','POST'])
def respuesta():
	print request.form
	return "hola " + request.form.get('username')    