import decimal
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as pltick
import os
import pandas as pd
import sqlite3

# Create a connection instance
conn = sqlite3.connect(os.path.realpath('../../data/db.sqlite3'))
cursor = conn.cursor()

query = """
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
        """

results = cursor.execute(query).fetchall()
print(results)
conn.close()

# Format the x-axis labels
x_map = {'BTC-USD':'Bitcoin', 'ETH-USD':'Ethereum', 'LTC-USD':'Litecoin'}

# Format the y-axis labels
fmt = '${x:,.2f}'
tick = pltick.StrMethodFormatter(fmt)

# Use the query results to structure the data
x_labels = [x_map.get(x[0]) for x in results]
raw_x_val = [decimal.Decimal(x[3]) for x in results]
x_val = range(0, len(raw_x_val))
y_val = raw_x_val

# Plot the data
plt.axes().yaxis.set_major_formatter(pltick.StrMethodFormatter(fmt))
plt.axes().yaxis.set_visible(False)
bar = plt.bar(x_val, y_val, color=['red'])
plt.title('Peak Prices On Coinbase Pro, In U.S. Dollars', fontweight='bold')
plt.xlabel('Cryptocurrency', fontweight='bold')
plt.xticks(x_val, x_labels)

# Place the y-axis value on top of each bar
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, '$%.2f' % height, ha='center', va='bottom')


# Save and show the figure
plt.savefig('peaks.png')
plt.show()
