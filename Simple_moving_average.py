! pip install pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader.data as web

def sma20_computation(ticker):
  start = dt.datetime(2020,1,1)
  end = dt.datetime(2021,2,12)
  df = web.DataReader(ticker , 'yahoo' , start, end)
  close_price = df["Close"]
  prices = []
  for i in close_price:
    prices.append(i)
  sma_20 = []
  #SMA Compute
  sma_compute = []
  a = 0
  while a <= len(prices) - 21:
    for n in range(a,a+20):
      sma_20.append(prices[n]) 
    sma = sum(sma_20)/20
    sma_20.clear()
    sma_compute.append(sma)
    a = a+1
    plt.plot(sma_compute, color='red')
    plt.plot(prices, color='blue')
    
    sma20_computation('MSFT')
