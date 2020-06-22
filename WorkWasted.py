# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:47:18 2020

@author: jpbsa
"""
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import ModelCheckpoint
from datetime import datetime as dt
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import random

class DataNew():
    def __init__(self):
        df_mortes2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        df_confirmados2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        df_recuperados2=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        self.confirmed = df_confirmados2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
        self.deaths = df_mortes2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
        self.recovered = df_recuperados2.drop(['Province/State', 'Lat', 'Long'], axis=1).groupby('Country/Region').sum()
        self.PreparaData()

    def PreparaData(self):
        timesteps = []
        total_infetados = []
        total_Days = []
        total_Deaths = []
        total_Recovered = []
        Country = []
        self.new_dataset = pd.DataFrame()
        Ground_Zero = dt.strptime('12/31/19','%m/%d/%y')
        iterator = 0
        for cols in self.confirmed.columns:
            for row in self.confirmed.iterrows():
                timesteps.append(cols)
                Country.append(self.confirmed.index[iterator])
                total_infetados.append(self.confirmed.iloc[iterator][cols])
                iterator +=1
            iterator = 0
            for row in self.deaths.iterrows():
                total_Deaths.append(self.deaths.iloc[iterator][cols])
                iterator +=1
            iterator = 0
            for row in self.recovered.iterrows():
                total_Recovered.append(self.recovered.iloc[iterator][cols])
                iterator +=1
            iterator = 0
        self.new_dataset['Country'] = Country
        self.new_dataset['Total_Cases'] = total_infetados
        self.new_dataset['Total_Recovered'] = total_Recovered
        self.new_dataset['Total_Deaths'] = total_Deaths
        #self.new_dataset['Days_Gone'] = total_Days
        pd.DataFrame.to_csv(self.new_dataset,'new_dataset.csv',index=False)

Data = DataNew()