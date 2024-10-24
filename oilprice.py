#https://medium.com/mlearning-ai/data-science-basics-time-series-analysis-with-oil-price-data-in-python-6f0b58321659
import os
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from scipy import stats
import statsmodels.api as sm
import seaborn as sns

data_dir = "./data/oil_price_analysis"
os.makedirs(data_dir, exist_ok=True)

start = dt.datetime(1950, 1, 1)
end = dt.datetime(2022, 5, 21)
wti_oil_price = web.DataReader('DCOILWTICO', 'fred', start, end)
# save the data
file_path = f"{data_dir}/DCOILWTICO.csv"
wti_oil_price.to_csv(file_path)
wti_oil_price

wti_oil_price = pd.read_csv(file_path, index_col="DATE", parse_dates=True)
print(wti_oil_price.shape)
wti_oil_price.tail(3)
wti_oil_price

plt.figure(figsize=(10, 6))
plt.plot(wti_oil_price)
plt.grid(axis="y")
plt.xlabel("Date")
plt.ylabel("Oil Price ($/Barrel)")
plt.show()

wti_oil_price.loc['2020-04-20']
wti_oil_price.loc['2020-04-20':'2020-04-30']
wti_oil_price.loc[dt.datetime(2020, 4, 20)]
wti_oil_price.loc['2020-04']
wti_oil_price.loc['2020']
