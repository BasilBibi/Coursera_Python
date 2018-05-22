import sqlite3


def getorgFromLine(line):
    pieces = line.split()
    org = pieces[1].split('@')[1]
    return org


def insertorg(cursor, org):
    cursor.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))


def updateorg(cursor, org):
    cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))


def getCountForEmai(cursor, org):
    cursor.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cursor.fetchone()
    return row


db_connection = sqlite3.connect('mod4_week2.sqlite')
cursor = db_connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')

cursor.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fh = open('mbox.txt')
for line in fh:
    if not line.startswith('From: '): continue
    org = getorgFromLine(line)
    row = getCountForEmai(cursor, org)
    if row is None:
        insertorg(cursor, org)
    else:
        updateorg(cursor, org)


db_connection.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])

cursor.close()
db_connection.close()
