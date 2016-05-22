"""Plot a histogram."""

import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # TODO: Your code here
    # Note: Returned DataFrame must have the same number of rows
    daily_returns = df.copy()
    # Compute daily returns for row 1 onwards
    # (1 to end over 0 to end -1) -1
    # Using .values is necessary because when given 2 data frames, Pandas
    # will try to match each row based on index when performing element wise
    # arithmetic operations.
    # daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 tp 0
    return daily_returns



def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')  # one month only
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Plot a histogram
    daily_returns.hist(bins=20)

    # Get mean and standard deviation
    mean = daily_returns['SPY'].mean()
    print "mean=",mean
    std = daily_returns['SPY'].std()
    print "std=",std

    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std,color='r',linestyle='dashed',linewidth=2)
    plt.grid()
    plt.show()

    # Compute kurtosis
    print daily_returns.kurtosis()

if __name__ == "__main__":
    test_run()
