**Project Title:** StockPicker

**Description:**

This project was developed for my CIIC4025 (Analysis and Design of Algorithms) course at the University of Puerto Rico at Mayagüez. Its main purpose is to select from a list of provided stocks based on the amount to invest and the specified timeframe for the rate of return for the stock.

**Usecase:**

A person has X amount of money to invest in a stock and he/she wants to maximize his/her investment based on stock historical data for a specific timeframe.  Maybe the person wants to maximize based on one month of historical projection or five months, a year, or 5 years. Since you want to have a diversified portfolio you can only pick 1 stock for each company, but if you still have money after picking the best stock for your timeframe your program can pick a fraction of the next stock. 

**Inputs:**

1. **List of Stocks:** This list contains stock data, including the stock name, price, and historical returns over different timeframes (1 month, 6 months, 1 year, and 5 years). The stock data is provided in a comma-separated file (CSV format) and is passed as a command line argument to the program. The format of the stock data is as follows:

    ```
    name,price,1M,6M,1Y,5Y
    GOOGL,134.98,5.18,28.72,33.87,76.46
    MSFT,323.23,0.45,17.98,33.25,182.75
    IBM,150.03,5.43,18.5,18.76,3.76
    HPQ,27.22,-13.06,-4.91,2.85,2.85
    ORCL,113.38,-2.68,29.58,66.63,122.21
    META,300.65,3.75,48.73,105.88,84.75
    TSLA,265.51,14.62,34.17,-14.15,1229.27
    ```

2. **Budget:** You specify the total amount of money available for stock investments.

3. **Timeframe:** You define the desired rate of return timeframe. Valid options include "1m" (1 month), "6m" (6 months), "1y" (1 year), and "5y" (5 years).

**Usage**

You can run the StockPicker program with a command like this:

```
python ./stockPicker.py stocks.csv 300 1m
```

This command instructs the program to:

- Use the stock data from the "stocks.csv" file.
- Inform the program that you have a budget of $300 for stock investments.
- Specify that you want to base your stock selection on the one-month rate of return.

**Output**

The program will then provide an output in the following format:

```
['TSLA', '0.26 GOOGL']
```

This output signifies that, with a $300 investment and a focus on the one-month rate of return, the optimal choice is to buy 1 stock of TSLA and 0.26 stocks of GOOGL.
