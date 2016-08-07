import sqlite3

db = sqlite3.connect('students')
c = db.cursor()
query = 'select name, id from students order by name;'
c.execute(query)
rows = c.fetchall()

for row in rows:
    print row[0]

db.close()

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()
