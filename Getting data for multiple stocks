# -*- coding: utf-8 -*-
"""
Spyder Editor
Seçilen hisse senetleri stock dizisi içerisinde tanımlanır. 
c1_price data frame üzerinde seçilen değerler her hisse senedi için yan yana gösterilir 
oh1cv_data sözlüğünde her hisse senedi için tüm veriler bulunur 

"""
import datetime as dt 
import yfinance as yf
import pandas as pd 
#incelemek istediğin stockları ekle  
stock =["AMZN","MSFT","GOOG"]
#incelemeye başlayacağın tarihi seç 
start = dt.datetime.today()-dt.timedelta(360)
#incelemenin biteceği tarih 
end = dt.datetime.today()
#empty dataframe whic will be filled with 
c1_price = pd.DataFrame()
oh1cv_data = {}
for ticker in stock: 
    c1_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
for ticker in stock:
    oh1cv_data[ticker] = yf.download(ticker,start,end)
