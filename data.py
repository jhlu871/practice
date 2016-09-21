# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:13:06 2016

@author: Jason
"""
import pandas as pd
import numpy as np
import talib as ta
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

def get_quandl_data(ticker,start_date = 0,end_date = 0):
    import quandl
    quandl.ApiConfig.api_key = "kNDy9NwFksBz5c1Y6mTP"
    if start_date == 0:
        if end_date == 0:
            data = quandl.get(ticker)
        else:
            data = quandl.get(ticker,end_date = end_date)
    else:
        if end_date == 0:
            data = quandl.get(ticker,start_date = start_date)
        else:
            data = quandl.get(ticker,start_date = start_date, end_date = end_date)
    return data
    
    
if __name__ == '__main__':
    data = get_quandl_data('SCF/CME_EC1_OR')
    data['pct_chg'] = data['Settle'].pct_change()
    data['sma50'] = ta.MA(data['Settle'].values,timeperiod=50)
    data['rsi3'] = ta.RSI(data['Settle'].values,timeperiod=3)
    data['trend'] = data['Settle']-data['sma50']
    
    # normalize test features    
    features = data.ix[49:,['trend','rsi3']]
    X = StandardScaler().fit_transform(features)

    # Transform labels to binary 1 or 0
    y = np.sign(data.ix[49:,['pct_chg']].values)
    y[y==0] = 1
    y = LabelEncoder().fit_transform(np.ravel(y))
    
    #split out out of sample data
    X_in,X_out = X[:-100], X[-100:]
    y_in,y_out = y[:-100],y[-100:]
    
    # split data into training and testing
    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size =.2, random_state = 42)
    
    # svm
    svm = SVC(C=1.0,kernel='rbf')
    svm.fit(X_train,y_train)
    pred = svm.predict(X_test)
    print(svm.score(X_test,y_test))
    print(svm.score(X_out,y_out))