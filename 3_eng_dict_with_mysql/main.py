import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="test",
)

cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictinary")
# Where condition
# query = cursor.execute("SELECT * FROM Dictinary WHERE var = '%s' " % word)
results = cursor.fetchall()
