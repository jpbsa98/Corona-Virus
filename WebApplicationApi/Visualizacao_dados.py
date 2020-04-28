#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





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

def grafico_pizza(df):
    df=df.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
    df2 = df[df.columns[-1]]
    
    df_index=[]
    df_value=[]
    df3=pd.DataFrame()
    print(df2)
    
    df_total=df_confirmados.drop(columns=['Country/Region','Lat','Long'])
    confirmados_total=df_total.sum()
    confirmados_total=max(confirmados_total)
    
    df2=df2.to_frame()
    
    for index, row in df2.iterrows():
        #print(index,(row[0]/confirmados_total)*100)
        
        df_index.append(index)
        df_value.append(format(((row[0]/confirmados_total)*100),'.2f'))
    df3['Pais']=df_index
    df3['Percentagem']=df_value
    df3['Percentagem'] = df3['Percentagem'].astype(float)
    df3=df3.sort_values(by=['Percentagem'],ascending=False)
    dftops=df3[:6]
    
    Total = df3['Percentagem'][6:].sum()
    d = {'Pais': ["Outros"], 'Percentagem': [Total]}
    dfoutros = pd.DataFrame(data=d)

    dftops=dftops.append(dfoutros)
    dftops=dftops.sort_values(by=['Percentagem'],ascending=False)
  
    print(dftops['Percentagem'].sum())
    #colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ff6666','#c2c2f0','#ffb3e6']
    colors =sns.color_palette("Blues",7)
    fig1, ax1 = plt.subplots()
    fig1.suptitle('Percentagem casos por país', fontsize=15, color='#0c3c6e')
    ax1.pie(dftops['Percentagem'], labels=dftops['Pais'],colors=colors,autopct='%1.1f%%', shadow=True)
    ax1.axis('equal')
    fig1.savefig('static/pizza.png')
    #plt.show()
    
grafico_pizza(df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'))



class Global():
       def __init__(self):
              fig, ax = plt.subplots(figsize=(20, 10))
              fig.suptitle('Mortes Corona Virus', fontsize=30, fontweight='bold')
              plt.xlabel('Dia', fontsize=20)
              plt.ylabel('Mortes', fontsize=20)
              
              ax.plot(mortes_total)
              
              start, end = ax.get_xlim()
              
              ax.xaxis.set_ticks(np.arange(start, end, 3))
              
              
              plt.xticks(rotation='vertical',fontsize=16)
              plt.yticks(np.arange(0, max(mortes_total)+1,max(mortes_total)/10),fontsize=16)
              
              ax.grid()
              fig.savefig('static/Deaths_Global.png')

              


              fig, ax = plt.subplots(figsize=(20, 10))
              fig.suptitle('Contaminados vs Recuperados', fontsize=30, fontweight='bold')
              plt.xlabel('Dia', fontsize=20)
              plt.ylabel('Casos', fontsize=20)
              
              
              ax.plot(confirmados_total,label='Confirmados')
              ax.plot(recuperados_total,label='Recupeados')
              start, end = ax.get_xlim()
              ax.xaxis.set_ticks(np.arange(start, end, 3))
              ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1,fontsize='15')
              plt.xticks(rotation='vertical')
              plt.yticks(np.arange(0, max(confirmados_total)+1, max(confirmados_total)/10))
              
              ax.grid()
              fig.savefig('static/Total.png')


              CasosAtuais=confirmados_total-recuperados_total-mortes_total
              fig, ax = plt.subplots(figsize=(20, 10))
              
              fig.suptitle('Casos Existentes', fontsize=30, fontweight='bold')
              plt.xlabel('Dia', fontsize=20)
              plt.ylabel('Casos Atuais', fontsize=20)
              
              ax.plot(CasosAtuais)
              start, end = ax.get_xlim()
              ax.xaxis.set_ticks(np.arange(start, end, 3))
              plt.xticks(rotation='vertical',fontsize=16)
              plt.yticks(np.arange(0, max(CasosAtuais)+1, max(CasosAtuais)/10),fontsize=16)
              
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
        fig.suptitle('Casos Corona Virus'+self.country, fontsize=30, fontweight='bold')
        plt.xlabel('Dia', fontsize=20)
        plt.ylabel('Casos Atuais', fontsize=20)
        ax.plot(self.pais_ativos,label="Ativos")
        ax.plot(self.pais_recuperados,label="Recuperados")
        ax.plot(self.pais_mortes,label="Mortes")
        ax.plot(self.pais_total,label="Total")
        ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1,fontsize='15')
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.arange(start, end, 3))
        plt.xticks(rotation='vertical')
        
        ax.grid()
        fig.savefig('static/Activos.png')
        #plt.show()


'''data_global=Global()

nome="Portugal"
pais=pais(nome)
pais.Graficos()'''





