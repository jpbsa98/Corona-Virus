# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:45:08 2020

@author: jpbsa
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from datetime import datetime as dt
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

confirmed_cases = pd.read_csv('Dados/time_series_2019-ncov-Confirmed.csv')
confirmed_deaths = pd.read_csv('Dados/time_series_2019-ncov-Deaths.csv')
confirmed_recovered = pd.read_csv('Dados/time_series_2019-ncov-Recovered.csv')

timesteps=5
# In[2]:


confirmed_recovered


# In[3]:


confirmed_cases['Province/State']


# In[4]:


class MLP():
    def __init__(self):
        pass
    def NormalizeData(self,df):
        self.scaler = MinMaxScaler(feature_range=(-1, 1))
        self.normalized = self.scaler.fit_transform(df)
        print(self.normalized)
        return self.normalized,self.scaler
        
    def Denormalize(self,dfNormalized):
        pass
    
    
    def PrepareData(self,timesteps):
        i = 0
        self.X = []
        self.Y = []
        while i in range(len(self.normalized - timesteps)):
            input_index = i + timesteps
            label_index = input_index + 1
            if(label_index < len(self.normalized)):
                self.X.append(self.normalized[i:input_index,0:1])
                self.Y.append(self.normalized[input_index:label_index,0:1])
            i+=1
        self.X = np.array(self.X)
        self.Y = np.array(self.Y)
    
    '''
    def Prepare_Data(self,dataset):
        x = dataset.drop(columns=['Total_Deaths'])
        self.X = x.to_numpy()
        y = dataset['Total_Deaths']
        self.Y = y.to_numpy()
        self.Y = self.Y.astype(float)
    '''
    def Build(self,janela,nmr_parametros):
        self.model = keras.Sequential()
        self.model.add(keras.layers.LSTM(512, input_shape=(janela, nmr_parametros), return_sequences=True))
        self.model.add(keras.layers.LSTM(128, return_sequences=True))
        self.model.add(keras.layers.LSTM(64, return_sequences=False))
        self.model.add(keras.layers.Dense(16, activation="relu", kernel_initializer="uniform"))
        self.model.add(keras.layers.Dense(1, activation="softmax"))
                       
    def RMSE(self,y_true,y_pred):
        return tf.cast(keras.backend.sqrt(keras.backend.mean(keras.backend.square(y_pred - y_true))),tf.float32)

    def Fit(self):
        self.model.compile(loss=self.RMSE,optimizer=keras.optimizers.Adam(),metrics=['mae',self.RMSE])
        self.history = self.model.fit(x=self.X,y=self.Y,epochs=53,batch_size=7,shuffle=False,verbose=True,validation_split=0.05)
    def Predict(self,data):
        result = self.model.predict(data,verbose=True)
        return result
        


# In[5]:


class Data():
    def __init__(self):
        self.PreparaData
    def PreparaData(self,confirmed,deaths,recovered):
        confirmedPortugal = confirmed[ confirmed['Country/Region'] != 'Italy'].index
        confirmed.drop(confirmedPortugal , inplace=True)
        confirmed = confirmed.drop(columns=['Province/State','Country/Region','Lat','Long'])
        deaths = deaths.drop(columns=['Province/State','Country/Region','Lat','Long'])
        recovered = recovered.drop(columns=['Province/State','Country/Region','Lat','Long'])
        timesteps = []
        total_infetados = []
        total_Days = []
        total_Deaths = []
        total_Recovered = []
        self.new_dataset = pd.DataFrame()
        Ground_Zero = dt.strptime('12/31/19','%m/%d/%y')
        for cols in confirmed.columns:
            timesteps.append(cols)
            total_infetados.append(confirmed[cols].sum())
            current_date = dt.strptime(cols,'%m/%d/%y')
            days_Gone = current_date - Ground_Zero
            total_Days.append(int(days_Gone.days))
        for cols in deaths.columns:
            total_Deaths.append(deaths[cols].sum())
        for cols in recovered.columns:
            total_Recovered.append(recovered[cols].sum())
        self.new_dataset['Total_Cases'] = total_infetados
        self.new_dataset['Total_Recovered'] = total_Recovered
        self.new_dataset['Total_Deaths'] = total_Deaths
        self.new_dataset['Days_Gone'] = total_Days
        self.new_dataset.set_index('Days_Gone')
        pd.DataFrame.to_csv(self.new_dataset,'Dados/new_dataset.csv')


# In[6]:


data = Data()
data.PreparaData(confirmed_cases,confirmed_deaths,confirmed_recovered)
print(data.new_dataset)


# In[7]:


model = MLP()
model.Build(timesteps,1)
data_norm,scaler=model.NormalizeData(data.new_dataset)
model.PrepareData(timesteps)
print(scaler)

# In[8]:


model.Fit()


# In[15]:

def forecast(model,df,timesteps,multisteps,data_norm,scaler):
    data_norm=pd.DataFrame(data_norm)
    input_seq=data_norm[-timesteps:].values
    inp=input_seq[:,0]
    
    
    predictions=list()
    
    inp = np.array(inp).astype('float32')
    print(inp)
    for step in range(1, multisteps+1):
        
        inp=inp.reshape(1,timesteps,1)
        
        yhat=model.Predict(inp)
        
        Denormalized = np.ndarray((1,4))
        Denormalized[0][0] = yhat
        Denormalized[0][1] = -1
        Denormalized[0][2] = -1
        Denormalized[0][3] = -1
        value = model.scaler.inverse_transform(Denormalized)
        print(value)
        predictions.append(value[0][0])
        #predictions.append(yhat[0][0])
        inp=np.append(inp[0],yhat)
        inp=inp[-timesteps:]
        print(inp)
        
    return predictions
print(scaler)
prediction = forecast(model,data.new_dataset,timesteps,10,data_norm,scaler)
# Denormalized = np.ndarray((1,4))
# Denormalized[0][0] = -1
# Denormalized[0][1] = -1
# Denormalized[0][2] = prediction
# Denormalized[0][3] = -1
# Denormalized1 = np.transpose(Denormalized)
# value = model.scaler.inverse_transform(Denormalized)
# print(value)
print(prediction)



plt.plot(np.arange(len(data.new_dataset)),(data.new_dataset['Total_Cases']), label='Days Gone with real data')
plt.plot(np.arange(len(data.new_dataset),len(data.new_dataset) + len(prediction)),(prediction), label='10 days LSTM prediction')
plt.title("LSTM's Prediction")
plt.xlabel('Days')
plt.ylabel('Confirmed Cases')
#plt.axis([1000,1250,10,25])
plt.legend()
plt.show();

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




