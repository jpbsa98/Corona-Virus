import Visualizacao_dados as data

from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/')
def test():
    dados = data.Global()
    return render_template('main.html', text = None)


@app.route('/Country')
def test1():
    dados = data.pais("Portugal")
    dados.Graficos()
    return render_template('main.html', text = None)