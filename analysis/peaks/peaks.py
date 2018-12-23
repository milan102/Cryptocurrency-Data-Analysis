import os
import sqlite3
import pandas as pd
import math
import matplotlib.pyplot as plt

# Create a connection instance
myConnection = sqlite3.connect(os.path.realpath('../../data/db.sqlite3'))

# create a Cursor object
myCursor = myConnection.cursor()

# Store the query as string
myQuery = """
        SELECT * , datetime(time, 'unixepoch', 'localtime') as date
        FROM candles
        WHERE (market, CAST(high as FLOAT)) IN
            (SELECT distinct market, MAX(CAST(high as FLOAT))
            FROM candles
            GROUP BY market)
        """

# Query the dataset
myCursor.execute(myQuery)

# Fetch the results
results = myCursor.execute(myQuery).fetchall()
print(results)

# Close the connection
myConnection.close()

# Play around with the imported Query results
x_labels = [x[0] for x in results]
y_val = [float(x[3]) for x in results]
x_val = range(0,len(y_val))
plt.bar(x_val, y_val, color=['blue'])
plt.title('Peak Prices of Cryptocurrency')
plt.xticks(x_val, x_labels)
plt.yticks(y_val)
plt.show()
