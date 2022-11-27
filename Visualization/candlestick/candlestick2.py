import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf 
import datetime as dt

start = dt.datetime(2020,8,1)
end = dt.datetime(2021,8,1)

data = web.DataReader('GME', 'yahoo', start, end)
# plt.plot(data['Close'])

# print(mpf.available_styles())
colors = mpf.make_marketcolors(up="#00ff00", 
                               down = "#ff0000", 
                               wick= "inherit", 
                               edge = "inherit", 
                               volume = "in")
mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)

mpf.plot(data, type = "candle", style=mpf_style, volume = True)

# print(data)

# plt.show()