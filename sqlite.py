import sqlite3

# Connect to db
conn = sqlite3.connect('test.db')
c = conn.cursor()

# Clean table on start
c.execute("DROP TABLE IF EXISTS Scores")

# Create Table
c.execute('''CREATE TABLE Scores (team TEXT, score INTEGER)''')

# Insert beginning scores
c.execute("INSERT INTO Scores VALUES ('White', 0), ('Blue', 0)")

# Select
for row in c.execute('SELECT * FROM Scores ORDER BY team'):
    print(row)

# Update Team White
c.execute("UPDATE Scores SET score = score + 1 WHERE team = 'White'")

# Select
for row in c.execute('SELECT * FROM Scores ORDER BY team'):
    print(row)

# Update Team Blue
c.execute("UPDATE Scores SET score = score + 1 WHERE team = 'Blue'")

# Select
for row in c.execute('SELECT * FROM Scores ORDER BY team'):
    print(row)

# Save and quit
conn.commit()
conn.close()
