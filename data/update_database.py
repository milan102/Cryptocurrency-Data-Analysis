import os

# Name of the file
DATABASE_NAME = "db.sqlite3"

# Updates the existing database
os.system("python3 main.py -p BTC-USD {}".format(DATABASE_NAME))
os.system("python3 main.py -p ETH-USD {}".format(DATABASE_NAME))
os.system("python3 main.py -p LTC-USD {}".format(DATABASE_NAME))
