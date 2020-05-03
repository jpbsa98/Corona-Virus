# Corona Vírus

O tema escolhido para o trabalho final da disciplina de Aprendizagem Automática II é o Corona Vírus e pretende-se dividir o trabalho nas seguintes fases:

- Análise do problema
- Planeamento do problema
- Análise dos dados
- Preparação dos dados
- Construção do modelo
- Visualização dos resultados

# Análise do problema

O Corona Vírus é uma doença infeciosa recente que tem causado graves consequências mundiais a nível económico, físico ou mental. Com este trabalho é pretendido termos uma melhor perceção sobre o tema e verificarmos a sua evolução em tempo real.

É importante referir que, todas as previsões efetuadas podem variar substancialmente devido ás medidas de prevenção e comportamento da sociedade nos diferentes países. As previsões efetuadas sejam a nível mundial ou de cada país apenas analisa o histórico de dados diários, sendo que, as diferentes medidas efetuadas por cada país podem melhorar ou piorar a evolução do vírus. O modelo não tem a capacidade de analisar as diferentes alterações na sociedade e, portanto, apenas analisa o passado.

# Planeamento do problema

Nesta fase o nosso foco é determinar os objetivos para o trabalho, bem como as vantagens na sua implementação.

Os objetivos estabelecidos para o trabalho são:

- Analisar os dados mundiais e os dados de cada país detalhadamente.
- Fazer previsões para os próximos 10 dias para cada país e a nível mundial.
- Apresentar gráficos com todos os resultados obtido.
- Criação de website capaz de mostrar toda a analise de dados efetuada.
- O website ser capaz de fazer previsões para cada país e a nível mundial.
- O website ser capaz de mostrar todas as previsões efetuadas.

#

# Base de dados

Toda a base de dados foi obtida no seguinte github:

[https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series](https://github.com/CSSEGISandData/COVID19/tree/master/csse_covid_19_data/csse_covid_19_time_series)

Os csv&#39;s utilizados foram:

- [Casos confirmados a nível global](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv) 
- [Mortes confirmadas a nível global](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv)
- [Recuperados confirmados a nível global](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv)

# Análise dos dados

- [Análise dos dados](https://github.com/jpbsa98/Corona-Virus/blob/master/DataAnalysisNotebook.ipynb)

# Preparação dos dados

- [Preparação dos dados](https://github.com/jpbsa98/Corona-Virus/blob/master/LstmPredictionsNotebook.ipynb)

# Construção do modelo LSTM e Visualização dos resultados

- [Contrução do modelo e visualização de resultados](https://github.com/jpbsa98/Corona-Virus/blob/master/LstmPredictionsNotebook.ipynb)

# Corona Alert(Web Site)


### Tutorial de utilização

#### Ambiente Anaconda

##### 1. Dependências

- conda install numpy
- conda install matplotlib
- conda install pandas
- conda install random
- conda install Flask
- conda install seaborn
- conda install sklearn
- conda install tensorflow
#### 2. Adicionar o projeto ao Flask

##### 2.1. Windows

cd C:\path\to\WEBapp\
set FLASK_APP=main.py

##### 2.2. Linux

cd C:\path\to\WEBapp\
export FLASK_APP=main.py

#### 3. Correr a aplicação

flask run

#### 4. Abrir a aplicação

Depois de correr a aplicação é necessário abrir o browser e colocar o seguinte endereço:

- [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
