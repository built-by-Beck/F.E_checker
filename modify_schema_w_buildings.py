import sqlite3

# Connect to the extinguisher.db database
conn = sqlite3.connect('extinguisher.db')

# Create a cursor object
cursor = conn.cursor()

# Add a new column for the building/section if it doesn't already exist
cursor.execute('''
    ALTER TABLE extinguishers
    ADD COLUMN building TEXT
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
