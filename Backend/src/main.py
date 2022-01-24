from flask import Flask, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route("/", methods=['GET'])#ruta para mostrar el home
def inicio_():
    return render_template('about.html')

@app.route("/portfolio", methods=['GET'])#ruta para mostrar el home
def portfolio_():
    return render_template('portfolio.html')

@app.route("/works", methods=['GET'])#ruta para mostrar el home
def works_():
    return render_template('works.html')

@app.route("/contact", methods=['GET'])#ruta para mostrar el home
def contact_():
    return render_template('contact.html')



@app.route("/olc2py1", methods=['GET'])#ruta para mostrar el home
def olc2py1_():
    return render_template('olc2py1.html')

if __name__ == "__main__":
    app.run(debug=True)