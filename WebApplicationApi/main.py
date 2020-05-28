import Visualizacao_dados as data
import RedeNeuronal1 as rede
from flask import Flask
from flask import render_template
from flask import request, redirect
import time


app = Flask(__name__)

@app.route('/')
def test():
    country = request.args.get('myCountry')
    if(request.args.get('prediction') is None):
        print('Normal request')
        image = "Activos.png"
    else:
        if(country == "World Wide"):
            country = None
        image = "lstm.png"
    if(country is None):
        dados = data.Global()
        country = "World Wide"
        #print(data.paises)
        return render_template('index.html',countries= data.paises, img = image,country=country, date = time.perf_counter(),value = max(data.confirmados_total),value2 = max(data.recuperados_total),value3 = max(data.mortes_total),value4 = max(data.confirmados_total)-max(data.recuperados_total)- max(data.mortes_total))
    else:
        print(' A obter dados de ' + country)
        dadosLocal = data.pais(country)
        dadosLocal.Graficos()
        #dados = rede.Data(country)
        #previsoes = rede.LSTM()
        #previsoes.forecast()

        return render_template('index.html',countries = data.paises,img = image,country=country,date = time.perf_counter(),value = max(dadosLocal.total),value3 = max(dadosLocal.pais_mortes),value2 = max(dadosLocal.pais_recuperados),value4 = (dadosLocal.pais_ativos[-1]))


@app.route('/Predict')
def Prediction():
    country = request.args.get('Country')
    if(request.args.get('Country') == "World Wide"):
        dados = data.Global()
        country = "World Wide"
        dados = rede.Data(country)
        previsoes = rede.LSTM()
        previsoes.forecast()
        return render_template('index.html',countries= data.paises,country=country, date = time.perf_counter(),value = max(data.confirmados_total),value2 = max(data.recuperados_total),value3 = max(data.mortes_total),value4 = max(data.confirmados_total)-max(data.recuperados_total)- max(data.mortes_total))
    else:
        print(' A obter dados de ' + country)
        dadosLocal = data.pais(country)
        dadosLocal.Graficos()
    print('ola')
    dados = rede.Data(country)
    previsoes = rede.LSTM()
    previsoes.forecast()
    return render_template('index.html',countries = data.paises,country=country,date = time.perf_counter(),value = max(dadosLocal.total),value3 = max(dadosLocal.pais_mortes),value2 = max(dadosLocal.pais_recuperados),value4 = max(dadosLocal.pais_ativos))