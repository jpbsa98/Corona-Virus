import Visualizacao_dados as data

from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/')
def test():
    dados = data.Global()
    return render_template('index.html', value = max(data.confirmados_total),value2 = max(data.recuperados_total),value3 = max(data.mortes_total),value4 = max(data.confirmados_total)-max(data.recuperados_total)- max(data.mortes_total))


@app.route('/Country')
def test1():
    dados = data.pais("Portugal")
    dados.Graficos()
    return render_template('main.html', text = None)