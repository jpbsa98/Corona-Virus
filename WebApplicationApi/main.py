import Visualizacao_dados as data

from flask import Flask
from flask import render_template
from flask import request, redirect
import time


app = Flask(__name__)

@app.route('/')
def test():
    dados = data.Global()
    country = request.args.get('myCountry')
    if(request.args.get('myCountry') is None):
        country = "World Wide"
        print(time.clock())
        return render_template('index.html',countries= data.paises,country=country, date = time.clock(),value = max(data.confirmados_total),value2 = max(data.recuperados_total),value3 = max(data.mortes_total),value4 = max(data.confirmados_total)-max(data.recuperados_total)- max(data.mortes_total))
    else:
        print(' A obter dados de ' + country)
        dadosLocal = data.pais(country)
        dadosLocal.Graficos()
        return render_template('index.html',countries = data.paises,country=country,date = time.clock(),value = max(dadosLocal.pais_total),value3 = max(dadosLocal.pais_mortes),value2 = max(dadosLocal.pais_recuperados),value4 = max(dadosLocal.pais_ativos))