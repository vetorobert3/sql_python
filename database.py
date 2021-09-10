import sqlite3

conn = sqlite3.connect('quotes.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("INSERT INTO quote VALUES ('Buddha', 'You only lose what you cling to.')")

print("Command executed succesfully...")
# Commit our command
conn.commit()

# Close our connection
conn.close()