import sqlite3

conn = sqlite3.connect('quotes.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM quote WHERE author like 'C%'")

items = c.fetchall()

for item in items:
    print(item)


#print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()