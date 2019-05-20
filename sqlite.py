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

c.execute("CREATE TABLE IF NOT EXISTS History (blueScore INTEGER, whiteScore INTEGER, \
                                               winner TEXT, datetime DATETIME)")

c.execute("INSERT INTO History VALUES ((SELECT score FROM Scores WHERE team = \
'Blue'), (SELECT score FROM Scores WHERE team = 'White'), (SELECT team FROM \
Scores WHERE score = (SELECT max(score) FROM Scores)), \
datetime('now','localtime'))")

# Select
for row in c.execute('SELECT * FROM Scores ORDER BY team'):
    print(row)
print

# Select
for row in c.execute('SELECT * FROM History'):
    print(row)
print

# Save and quit
conn.commit()
conn.close()
