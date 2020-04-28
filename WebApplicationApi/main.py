import Visualizacao_dados as data

from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/')
def test():
    dados = data.Global()
    country = request.args.get('country')
    if(request.args.get('country') is None):
        print('Dados globais')
        return render_template('index.html', value = max(data.confirmados_total),value2 = max(data.recuperados_total),value3 = max(data.mortes_total),value4 = max(data.confirmados_total)-max(data.recuperados_total)- max(data.mortes_total))
    else:
        print(' A obter dados de ' + country)
        dadosLocal = data.pais(country)
        dadosLocal.Graficos()
        return render_template('index.html')