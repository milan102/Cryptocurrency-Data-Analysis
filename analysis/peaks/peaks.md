# A Look Back At Peak Cryptocurrency Prices

The underlying motivation for cryptocurrency investors is to make money.  They sign-up on digital currency exchange websites, transfer funds into their accounts, make purchases, and hopefully  sell for a profit at some point in the future.

But at what cost? Let's figure out the highest price that Bitcoin, Ethereum, and Litecoin reached on one of cryptocurrency's most prominent exchanges, [Coinbase Pro](https://pro.coinbase.com/) (previously known as GDAX).


## Data
We query our database to get the resulting table and chart.

```sql
SELECT *, datetime(time, 'unixepoch', 'localtime') as date
    FROM candles
    WHERE (market, time) IN
        (SELECT market, MIN(time)
        FROM candles
        WHERE (market, CAST(high as FLOAT)) IN
            (SELECT market, MAX(CAST(high as FLOAT))
            FROM candles
            GROUP BY market)
        GROUP BY market)
```

market | date (PST) | high
------ | ---------- | ----
BTC-USD | 2017-12-17 04:36:00 | $19,891.99
ETH-USD | 2018-01-13 13:03:00 | $1,419.96
LTC-USD | 2017-12-12 06:11:00 | $420.00

![Peak cryptocurrency prices on Coinbase Pro](https://github.com/milan102/Cryptocurrency-Data-Analysis/blob/master/analysis/peaks/peaks.png)


## Analysis
 - On *December 12th, 2017*, Litecoin, the least popular of the group, was the first to reach its all-time-high.

 - Bitcoin followed shortly after on *December 17th, 2017*, however it took Ethereum about a month, *January 13th, 2018*.

 - Bitcoin's and Litecoin's peaks occurred in the early morning (relative to the PST timezone), *4:36 AM* and *6:11 AM*, respectively. For Ethereum, this was in the afternoon, *1:03 PM*.

 - Litecoin's peak price is an integer, precisely *$420*. [Was Elon Musk considering taking it private?](https://twitter.com/elonmusk/status/1026872652290379776)


## Conclusion
Hindsight is nice. From back then to the time of this writing (December 2018), prices have been trending downward. Traders would not have been wrong to remain optimistic about cryptocurrency until the 2017 holiday season, and then change to a pessimistic attitude in early 2018. Will the correct strategy change to optimism in 2019?

All code used to perform this analysis is available [here](https://github.com/milan102/Cryptocurrency-Data-Analysis).
