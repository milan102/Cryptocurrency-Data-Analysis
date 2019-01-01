# The Lowest Cryptocurrency Prices on Coinbase Pro

Let's figure out the lowest price that Bitcoin, Ethereum, and Litecoin reached on one of cryptocurrency's most prominent exchanges, [Coinbase Pro](https://pro.coinbase.com/) (previously known as GDAX).


## Data
We query our database to get the resulting table and chart. Note that the "greater than" conditions in the query are meant to eliminate values that aren't realistic, because orders at a normal volume would not have been filled at prices less than the specified numbers.

```sql
SELECT *, datetime(time, 'unixepoch', 'localtime') as date
    FROM candles
    WHERE (market, time) IN
        (SELECT market, MIN(time)
        FROM candles
        WHERE (market, CAST(low as FLOAT)) IN
            (SELECT market, MIN(CAST(low as FLOAT))
            FROM candles
    WHERE (market = 'BTC-USD' AND (CAST(low as FLOAT)) > 198.01)
    OR (market = 'ETH-USD' AND (CAST(low as FLOAT)) > 0.1)
    OR (market = 'LTC-USD' AND (CAST(low as FLOAT)) > 0)
            GROUP BY market)
        GROUP BY market)
```

market | date (PST) | low (USD)
------ | ---------- | ---------
BTC-USD | 2015-08-24 17:55:00 | $198.02
ETH-USD | 2016-12-06 02:16:00 | $5.81
LTC-USD | 2016-09-01 10:12:00 | $3.26

![Lowest cryptocurrency prices on Coinbase Pro](https://github.com/milan102/Cryptocurrency-Data-Analysis/blob/master/analysis/lows/lows.png)


## Analysis
 - Perhaps unsurprisingly, Bitcoin was the first to reach its all-time-low, on *August 24th, 2015*.  Cryptocurrencies generally follow large downward movements of stocks, so this was probably caused by [the global stock market selloff](https://www.cnbc.com/2015/09/25/what-happened-during-the-aug-24-flash-crash.html).

 - The *$198.02* U.S. dollar low is ignoring the fact that [a glitch caused the listed price of Bitcoin to drop to 6 cents](https://www.newsbtc.com/2017/04/16/gdax-bitcoin-price-briefly-crashes-us0-06-system-maintenance/)  and that we are ignoring unrealistic numbers for orders on January 14th, 2015, due to the historical API data citing extremely low volume and an overall lack of sufficient information...[however that day was valid for a huge drop in Bitcoin's price](https://www.cnbc.com/2015/01/14/bitcoin-falls-below-200-making-some-investors-worry-about-downward-spiral.html).

 - Ethereum's price drop was [hypothesized to be from growing uncertainty about the future of the project, caused from multiple hard forks](https://www.coindesk.com/ethereums-price-woes-continue-digital-currency-hits-9-month-low).

 - From these lows to [their eventual peaks](https://github.com/milan102/Cryptocurrency-Data-Analysis/blob/master/analysis/peaks/peaks.md), the increase was roughly: *100x* for Bitcoin, *244x* for Ethereum, and *128x* for Litecoin.

## Conclusion
Cryptocurrency prices will probably never be this low again. This was interesting to look into because the prices displayed above are *realistic* entry points that would have made long-term investors the most money.

All code used to perform this analysis is available [here](https://github.com/milan102/Cryptocurrency-Data-Analysis).
