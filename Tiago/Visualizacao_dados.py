#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


df_mortes=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df_confirmados=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_recuperados=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')


# In[7]:


df_confirmados.head()


# In[8]:


df_recuperados.head()


# In[9]:


df_mortes=df_mortes.drop(columns=['Country/Region','Lat','Long'])


# In[14]:


mortes_total=df_mortes.sum()
mortes_total.head()


fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(mortes_total)
plt.xticks(rotation='vertical')
plt.yticks(np.arange(0, max(mortes_total)+1,max(mortes_total)/10))
ax.set(xlabel='Dia', ylabel='Mortes',
       title='Mortes Corona Virus')
ax.grid()

plt.show()


# In[11]:


df_confirmados=df_confirmados.drop(columns=['Country/Region','Lat','Long'])
df_recuperados=df_recuperados.drop(columns=['Country/Region','Lat','Long'])


# In[18]:


confirmados_total=df_confirmados.sum()
recuperados_total=df_recuperados.sum()


fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(confirmados_total,label='Confirmados')
ax.plot(recuperados_total,label='Recupeados')
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1,fontsize='15')
plt.xticks(rotation='vertical')
plt.yticks(np.arange(0, max(confirmados_total)+1, max(confirmados_total)/10))
ax.set(xlabel='Dia',
       ylabel='Casos',
       title='Contaminados vs Recuperados')
ax.grid()

plt.show()


# In[16]:


CasosAtuais=confirmados_total-recuperados_total-mortes_total
CasosAtuais
fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(CasosAtuais)
plt.xticks(rotation='vertical')
plt.yticks(np.arange(0, max(CasosAtuais)+1, max(CasosAtuais)/10))
ax.set(xlabel='Dia', ylabel='CasosAtuais',
       title='Casos Existentes')
ax.grid()

plt.show()


# In[53]:


class pais():
    def __init__(self):
        pass
    def PrepareData(self,nome):
        df_mortes2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        df_confirmados2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        df_recuperados2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')


        confirmados_pais = df_confirmados2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
        mortes_pais = df_mortes2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
        recuperados_pais = df_recuperados2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()


        df_pais_totais=confirmados_pais.loc[[nome]]
        df_pais_ativos=confirmados_pais.loc[[nome]]-recuperados_pais.loc[[nome]]-mortes_pais.loc[[nome]]
        df_pais_recuperados=recuperados_pais.loc[[nome]]
        df_pais_mortes=mortes_pais.loc[[nome]]


        df_pais_ativos.head()

        self.pais_ativos=df_pais_ativos.sum()

        self.pais_recuperados=df_pais_recuperados.sum()

        self.pais_mortes=df_pais_mortes.sum()

        self.pais_total=df_pais_totais.sum()
    def Graficos(self,nome):

        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(self.pais_ativos,label="Ativos")
        ax.plot(self.pais_recuperados,label="Recuperados")
        ax.plot(self.pais_mortes,label="Mortes")
        ax.plot(self.pais_total,label="Total")
        ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1,fontsize='15')
        plt.xticks(rotation='vertical')
        ax.set(xlabel='Dia', ylabel='Casos Atuais',
               title='Casos Corona Virus ' +nome)
        ax.grid()

        plt.show()


# In[54]:


data = pais()
nome="Portugal"
data.PrepareData(nome)
data.Graficos(nome)


# In[ ]:




