import sqlite3

db = sqlite3.connect("mlbb.db")
cursor = db.cursor()
sql = "SELECT * from mlbb;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()