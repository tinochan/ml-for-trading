"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    plt.title('IBM High')
    plt.ylabel('$')
    plt.plot(df['High']) #Or df['High'].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
