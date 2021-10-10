# Creator : MRD3F417 [!] Dont Copy Kid - I See You - Discord : MƦ.Ɗ3Ƒ417#8277
# BlackGuard Team - Discord : discord.gg/4DbuQRg6YX
# Python 3 - Windows / Linux
# Get Live Cryptocurrency Data

#███╗░░░███╗██████╗░░░░██████╗░██████╗░███████╗░░██╗██╗░░███╗░░███████╗
#████╗░████║██╔══██╗░░░██╔══██╗╚════██╗██╔════╝░██╔╝██║░████║░░╚════██║
#██╔████╔██║██████╔╝░░░██║░░██║░█████╔╝█████╗░░██╔╝░██║██╔██║░░░░░░██╔╝
#██║╚██╔╝██║██╔══██╗░░░██║░░██║░╚═══██╗██╔══╝░░███████║╚═╝██║░░░░░██╔╝░
#██║░╚═╝░██║██║░░██║██╗██████╔╝██████╔╝██║░░░░░╚════██║███████╗░░██╔╝░░
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚═╝░░░░░░░░░░╚═╝╚══════╝░░╚═╝░░░


import numpy as np
import pandas as pd


import yfinance as yf


import plotly.graph_objs as go


data = yf.download(tickers='BTC-USD', period = '22h', interval = '15m')


fig = go.Figure()


fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))


fig.update_layout(
    title='Bitcoin live share price | Dont Copy Kid - I See You - Discord : MƦ.Ɗ3Ƒ417#8277 ',
    yaxis_title='Bitcoin Price (kUS Dollars) | MR.D3F417')


fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)


fig.show()