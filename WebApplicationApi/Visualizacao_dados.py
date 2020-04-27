#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter



df_mortes=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df_confirmados=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_recuperados=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

df_confirmados.head()
df_recuperados.head()
df_mortes=df_mortes.drop(columns=['Country/Region','Lat','Long'])

mortes_total=df_mortes.sum()
mortes_total.head()

df_confirmados=df_confirmados.drop(columns=['Country/Region','Lat','Long'])
df_recuperados=df_recuperados.drop(columns=['Country/Region','Lat','Long'])

confirmados_total=df_confirmados.sum()
recuperados_total=df_recuperados.sum()



class Global():
       def __init__(self):
              fig, ax = plt.subplots(figsize=(20, 10))
              ax.plot(mortes_total)
              
              
              



              start, end = ax.get_xlim()
              ax.xaxis.set_ticks(np.arange(start, end, 3))
              
              plt.xticks(rotation='vertical')
              plt.yticks(np.arange(0, max(mortes_total)+1,max(mortes_total)/10))
              ax.set(xlabel='Dia', ylabel='Mortes',
                     title='Mortes Corona Virus')
              ax.grid()
              fig.savefig('static/Deaths_Global.png')

              fig, ax = plt.subplots(figsize=(20, 10))
              ax.plot(confirmados_total,label='Confirmados')
              ax.plot(recuperados_total,label='Recupeados')
              start, end = ax.get_xlim()
              ax.xaxis.set_ticks(np.arange(start, end, 3))
              ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1,fontsize='15')
              plt.xticks(rotation='vertical')
              plt.yticks(np.arange(0, max(confirmados_total)+1, max(confirmados_total)/10))
              ax.set(xlabel='Dia',
                     ylabel='Casos',
                     title='Contaminados vs Recuperados')
              ax.grid()
              fig.savefig('static/Total.png')


              CasosAtuais=confirmados_total-recuperados_total-mortes_total
              fig, ax = plt.subplots(figsize=(20, 10))
              ax.plot(CasosAtuais)
              start, end = ax.get_xlim()
              ax.xaxis.set_ticks(np.arange(start, end, 3))
              plt.xticks(rotation='vertical')
              plt.yticks(np.arange(0, max(CasosAtuais)+1, max(CasosAtuais)/10))
              ax.set(xlabel='Dia', ylabel='CasosAtuais',
                     title='Casos Existentes')
              ax.grid()
              fig.savefig('static/Activos.png')



class pais():
    def __init__(self,_country):
       self.country = _country
       self.PrepareData()
    def PrepareData(self):
        df_mortes2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        df_confirmados2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        df_recuperados2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')


        confirmados_pais = df_confirmados2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
        mortes_pais = df_mortes2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
        recuperados_pais = df_recuperados2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()


        df_pais_totais=confirmados_pais.loc[[self.country]]
        df_pais_ativos=confirmados_pais.loc[[self.country]]-recuperados_pais.loc[[self.country]]-mortes_pais.loc[[self.country]]
        df_pais_recuperados=recuperados_pais.loc[[self.country]]
        df_pais_mortes=mortes_pais.loc[[self.country]]


        df_pais_ativos.head()

        self.pais_ativos=df_pais_ativos.sum()

        self.pais_recuperados=df_pais_recuperados.sum()

        self.pais_mortes=df_pais_mortes.sum()

        self.pais_total=df_pais_totais.sum()
    def Graficos(self):

        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(self.pais_ativos,label="Ativos")
        ax.plot(self.pais_recuperados,label="Recuperados")
        ax.plot(self.pais_mortes,label="Mortes")
        ax.plot(self.pais_total,label="Total")
        ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1,fontsize='15')
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.arange(start, end, 3))
        plt.xticks(rotation='vertical')
        ax.set(xlabel='Dia', ylabel='Casos Atuais',
               title='Casos Corona Virus ' +self.country)
        ax.grid()
        fig.savefig('Image.png')
        #plt.show()


data_global=Global()

nome="Portugal"
pais=pais(nome)
pais.Graficos()





