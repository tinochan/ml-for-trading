"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("../data/IBM.csv")
    # TODO: Your code here

    plt.figure(1)

    #high
    plt.subplot(121)
    plt.title('IBM High')
    plt.ylabel('$')
    plt.plot(df['High']) #Or df['High'].plot() to show the graph immediately

    #close & adj close
    plt.subplot(122)
    plt.title('IBM Close & Adj Close')
    plt.ylabel('$')
    plt.plot(df[['Close','Adj Close']])
    plt.grid(True)

    plt.show()  # must be called to show plots

if __name__ == "__main__":
    test_run()
