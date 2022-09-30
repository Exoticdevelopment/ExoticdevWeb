from unicodedata import name
from flask import Flask , render_template
#Con render template en vez de retornar un texto 
#puedo retornar una plantilla de html

app= Flask(__name__)

@app.route('/')#Asi creamos rutas
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')


if __name__ == '__main__':
    app.run(debug=True)
#Es para no estar apagando y prendiendo el server con cada modificacion , 
# con eso pondremos el server en modo prueba y cualquier actualizacion se montara de una , 
# Cada vez que modifiquemos algo , el servidor se va a reiniciar






