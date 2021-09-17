import sqlite3

conn = sqlite3.connect('quotes.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM quote")
#print(c.fetchone()[1])
#print(c.fetchmany(2))
items = c.fetchall()
for item in items:
    print(item[0] + ": " + item[1])

#print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()