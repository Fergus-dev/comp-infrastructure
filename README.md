# Automating data flow from Yahoo Finance

In this project I write a script and use Github Workflows to run it automatically every Saturday morning. The script downloads the stock performance data for the five FAANG companies for the past 5 days and plots this data.

To clone this repository and use the code yourself, you will need to have Python installed on your machine, as well as a code editor (I used VS Code). Please see below for instruction on how to download each of these below:

- (`python`)[https://www.python.org/downloads/]
- (`vs code`)[https://code.visualstudio.com/docs/setup/setup-overview]

In this project I use three Pyhton packages: `yfinance`, `pandas`, and `matplotlib`. Instructions for downloading and using these packages follow below:

## Installing the necessary packages

You can install the all three packages on your machine by using the pip command. The method for doing so for each package is as follows:

- (`yfinance`)[http://www.geeksforgeeks.org/python/how-to-install-yfinance-with-python-pip/]
- (`pandas`)[https://www.pythoncentral.io/how-to-install-pandas-in-python/]
- (`matplotlib`)[https://matplotlib.org/stable/install/index.html]

## Project explanation

You should begin with the `problems.ipynb` notebook. Each step within that notebook can be explained as follows:

- Code cell 1: This code cell defines a function called get_data(), the purpose of which is to is to download, clean and save data for the five 'FAANG' stocks for the 5 day period directly preceding the day on which the code is run. It uses the Pandas `pd.Timestamp` function to get the current date and time ((reference used)[https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior]). Then, the yfinance package `yf.download` is used to download the data ((reference used)[https://ranaroussi.github.io/yfinance/reference/yfinance.ticker_tickers.html]). Then the data is converted into a Pandas Multiindex object and saved as a .csv file.

- Code cell 2: This code cell plots the data. I use matplolib packages such as `plt.figure` to plot the .csv data. I add a legend corresponding the tickers using the `ax.legend` function, and perform other operations on the plot to improve readability which are explained in the `problems.ipynb` notebook. Key references used in this section can be found (here)[https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html] for the basic plotting, and (here)[https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html] for saving the plot as a .png file. I referred directly to the `matplotlib` documentation (here)[https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html] when creating the legend and making other additions and changes to the plot.

- The rest of the notebook details how I made my script executable directly from my terminal by simply typing in "faang". This relates to Windows Powershell specifically. Windows ignored the shebang line I had added into my script, so I had to find another way to make it executable from the terminal. The solution I found was to create a .bat file.








## Reference guide
Below is a list of references that point to different parts of this project:


### Problems.ipynb (problem 1)
- [Formatting of datetime output](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
- [Creation of a Multi index pandas dataframe object](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)

### Problems.ipynb (problem 2)
- [Adjusting the style and layout of the plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)