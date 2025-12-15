#!/C:/Users/fmtie/anaconda3/python

# reference: https://www.geeksforgeeks.org/linux-unix/using-shebang-in-linux/

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    current_date_time = pd.Timestamp.now().strftime('%Y%m%d-%H%M%S') #reference: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    file_path = f'data/{current_date_time}.csv'
    faang_stock_data_past_5_days = yf.download('meta aapl amzn nflx goog', period="5d") # reference: https://ranaroussi.github.io/yfinance/reference/yfinance.ticker_tickers.html
    faang_stock_data_frame = pd.DataFrame(faang_stock_data_past_5_days)
    pd.MultiIndex.from_frame(faang_stock_data_frame)
    faang_stock_data_frame.to_csv(file_path)

    return file_path

# this runs the function, while also storing the file path used which I need for my next function
file_path = get_data()

# reading in the csv file specifying the two header rows (as I initially made this a multi-index dataframe)
# then creating a figure and subplots
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
def plot_data():
    current_date_time = pd.Timestamp.now().strftime('%Y%m%d-%H%M%S') #reference: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    df = pd.read_csv(file_path, index_col=0, header=[0,1])
    closes = df['Close']
    tickers = closes.columns
    fig = plt.figure(figsize=(20, 12))
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_title({current_date_time})
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price (USD)')
    ax1.plot(closes[tickers], lw=0.6, ls='--')
    ax1.legend(tickers)
    return current_date_time

current_date_time = plot_data()
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
# As per documentation, if format argument is not set, it is inferred from file extension (.png)
plt.savefig(f'plots/{current_date_time}.png')