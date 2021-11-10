import sqlite3

# Query the database and return all records
def show_all():
    # Connect to database
    conn = sqlite3.connect('quotes.db')
    # Create a cursor
    c = conn.cursor()

    # Query the database - Order by
    c.execute("SELECT rowid, * FROM quote")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()

    # Close our connection
    conn.close()


# Add a new quote
def add_quote(author, quote):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()

    c.execute("INSERT INTO quote VALUES (?,?)", (author, quote))

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Delete quote
def delete_quote(id):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()

    c.execute("DELETE from quote WHERE rowid = (?)", id)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Add many quotes
def add_many_quotes(list):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()

    c.executemany("INSERT INTO quote VALUES (?,?)", (list))  

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


# Lookup with Where
def author_lookup(author):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * from quote WHERE author = (?)", (author,))
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()



