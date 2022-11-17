import mysql.connector

Connection =mysql.connector.connect(
    user = 'root', password='root', host='mysql', port="3306", database='db'
)
print("DB Connection.cursor")

cursor =Connection.cursor()
cursor.execute('Select * FROM students')
students =cursor.fetchall()
Connection.close()

print(students)
