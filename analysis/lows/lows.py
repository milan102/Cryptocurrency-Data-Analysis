import os
import sqlite3
import pandas as pd
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as pltick

# Create a connection instance
conn = sqlite3.connect(os.path.realpath('../../data/db.sqlite3'))
cursor = conn.cursor()

query = """
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
        """

results = cursor.execute(query).fetchall()
print(results)
conn.close()

# Format the y-axis values
fmt = '${x:,.0f}'
tick = pltick.StrMethodFormatter(fmt)

# Format the x-axis values
x_map = {"BTC-USD":"Bitcoin", "ETH-USD":"Ethereum", "LTC-USD":"Litecoin"}

# Use the query results to structure the data
x_labels = [x_map.get(x[0]) for x in results]
raw_x_val = [float(x[3]) for x in results]
x_val = range(0,len(raw_x_val))
y_val = raw_x_val

# Plot the data
plt.axes().yaxis.set_major_formatter(pltick.StrMethodFormatter(fmt))
plt.bar(x_val, y_val, color=['blue'])
plt.title('Lowest Prices On Coinbase Pro, In U.S. Dollars', fontweight='bold')
plt.xlabel('Cryptocurrency', fontweight='bold')
plt.xticks(x_val, x_labels)
plt.yticks(y_val)
plt.savefig('lows.png')
plt.show()
