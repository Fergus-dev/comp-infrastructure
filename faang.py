import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
        # getting the current date and time to use in the file name
        current_date_time = pd.Timestamp.now().strftime('%Y%m%d-%H%M%S')
        file_path = f'C:/Users/fmtie/OneDrive/Desktop/comp-infrastructure/data/{current_date_time}.csv'
        # here I specify the tickers of each company as arguments in a single string, and specify the period to be the past 5 days as another argument
        faang_stock_data_past_5_days = yf.download('meta aapl amzn nflx goog', period="5d")
        # converting data to a dataframe
        faang_stock_data_frame = pd.DataFrame(faang_stock_data_past_5_days)
        # setting multi-index for better organization
        pd.MultiIndex.from_frame(faang_stock_data_frame)
        faang_stock_data_frame.to_csv(file_path)
        # returning updated file path for use in another function to be called later
        return file_path

# running the function while saving the returned file path for use in later function
file_path = get_data()

def plot_data():
    # getting the current date and time to use in the plot title
    current_date_time = pd.Timestamp.now().strftime('%Y%m%d-%H%M%S')
    # reading the csv file saved earlier
    faang_df = pd.read_csv(file_path, index_col=0, header=[0,1])
    # extracting the 'Close' prices for plotting
    closes = faang_df['Close']
    # getting the tickers for labeling
    tickers = closes.columns
    # creating the plot
    fig = plt.figure(figsize=(20, 12))
    ax1 = fig.add_subplot(2, 2, 1)
    # styling the plot
    ax1.set_title({current_date_time})
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price (USD)')
    ax1.plot(closes[tickers], lw=0.6, ls='--')
    ax1.legend(tickers)
    # saving the plot to a specified directory with current date and time in the filename
    plt.savefig(f'C:/Users/fmtie/OneDrive/Desktop/comp-infrastructure/plots/{current_date_time}.png')

# calling the funtion
plot_data()