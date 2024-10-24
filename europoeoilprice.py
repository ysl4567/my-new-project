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
brent_oil_price = web.DataReader('DCOILBRENTEU', 'fred', start, end)
# save the data
file_path = f"{data_dir}/DCOILBRENTEU.csv"
brent_oil_price.to_csv(file_path)
brent_oil_price = pd.read_csv(file_path, index_col="DATE", parse_dates=True)
print(brent_oil_price.shape)
brent_oil_price.tail(3)
brent_oil_price
