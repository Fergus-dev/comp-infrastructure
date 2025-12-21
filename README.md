# Automating data flow from Yahoo Finance

In this project I write a script and use Github Workflows to run it automatically every Saturday morning. The script downloads the stock performance data for the five FAANG companies for the past 5 days and plots this data.

To clone this repository and use the code yourself, you will need to have Python installed on your machine, as well as a code editor (I used VS Code). Please see below for instruction on how to download each of these below:

- [`python`](https://www.python.org/downloads/)
- [`vs code`](https://code.visualstudio.com/docs/setup/setup-overview)

In this project I use three Pyhton packages: `yfinance`, `pandas`, and `matplotlib`. Instructions for downloading and using these packages follow below:

## Installing the necessary packages

You can install the all three packages on your machine by using the pip command. The method for doing so for each package is as follows:

- (`yfinance`)[http://www.geeksforgeeks.org/python/how-to-install-yfinance-with-python-pip/]
- (`pandas`)[https://www.pythoncentral.io/how-to-install-pandas-in-python/]
- (`matplotlib`)[https://matplotlib.org/stable/install/index.html]

## Project explanation

You should begin with the `problems.ipynb` notebook. Each step within that notebook can be explained as follows:

### Part 1

The first part of the project consists of a markdown cell and a code cell. In the code cell I define a function called get_data(), the purpose of which is to is to download, clean and save data for the five 'FAANG' stocks for the 5 day period directly preceding the day on which the code is run. I use the Pandas `pd.Timestamp` function to get the current date and time. Then, I use the yfinance package `yf.download` to download the data. Finally the data is converted into a Pandas Multiindex object and saved as a .csv file.

Make sure to update the file path variable so that it points to somewhere on your machine if running this part of the code yourself.

#### References used in this section
- [pd.Timestamp](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
- [yfinance](https://ranaroussi.github.io/yfinance/reference/yfinance.ticker_tickers.html)
- [Multiindexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html)

### Part 2

The second part of the project also consists of a markdown cell and a code cell. In the code cell I use matplolib packages such as `plt.figure` to plot the .csv data. I add a legend corresponding to the tickers using the `ax.legend` function, and perform other operations on the plot to improve readability which are explained in the `problems.ipynb` notebook.

#### References used in this section
- [Basic plotting](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
- [Saving plot as png file](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html)
- [Styling the plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html)

### Part 3

The third section of the notebook is a single markdown cell rather than a code cell, and deals with making the script executable from my terminal. I am a Windows user, so this relates to the Windows Powershell specifically. How I achieved this is explained in writing and screenshots are included.

#### References used in this section
- [Copilot conversation](https://copilot.microsoft.com/shares/5yk87y43HYjypoqf47ZED)

### Part 4

The final section of the notebook is also a markdown cell and explains how I set up a Github Workflow to automatically run my script every Saturday morning.

#### References used in this section

- [Github workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/add-scripts)
- [Github workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [YAML syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Github actions](https://blog.devops.dev/a-complete-guide-to-creating-github-actions-pipeline-with-yaml-templates-c57f2dbc2d0c)