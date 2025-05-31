import sqlite3
import csv

conn = sqlite3.connect('Company.db3')
cur = conn.cursor()

with open('item.csv', 'r') as f:
    reader = csv.reader(f)
    for rows in reader:
        cur.execute('INSERT INTO Item (ItemName, ItemType, ItemColour) VALUES (\t, \t, \t)', rows)

conn.commit()
conn.close()