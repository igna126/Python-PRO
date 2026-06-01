from flask import Flask
import random
app = Flask(__name__)

nombre = "Ignacio"
numerosecrerto = random.randint(1,10)
facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo p",
    "Según un estudio realizado en 2018, más del 50(%) de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.",
    "El estudio de la adicción tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

@app.route("/")
def hello_world():
    return f'''<h1>Hello, World!</h1>
    <p>Sitio Creado por: {nombre} </p>
    <a href = "/datos"> Ver Datos</a>
    '''
@app.route("/datos")
def datos():
    return f'''
    <h1> Este es un dato sobre la dependencia tecnológica: </h1>
    <p> {random.choice(facts_list)} </p>
    <a href = "/datos">Ver otro dato</a>
    <a href = "/">Ir a Inicio</a>
    <a href = "/color/blue">Ver texto de color</a>
    '''

@app.route("/color/<string:color>")
def color(color):
    return f'''
    <h1 style="color:{color}"> Este texto está en el color {color} </h1>
    <a href = "/">Ir a Inicio</a>
    '''



@app.route("/secret")
def moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return f"<h1>🪙 El destino ha hablado:</h1><p>Ha salido: <strong>{resultado}</strong></p>"


if __name__ == "__main__":
    app.run(debug=True)
