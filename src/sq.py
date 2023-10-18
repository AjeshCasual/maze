import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="IDKpassword@1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE level1")
mycursor.execute("CREATE TABLE Level1 (sid VARCHAR(255), score INT(255))")
mycursor.execute("CREATE DATABASE level2")
mycursor.execute("CREATE TABLE Level2 (sid VARCHAR(255), score INT(255))")
mycursor.execute("CREATE DATABASE level3")
mycursor.execute("CREATE TABLE Level3 (sid VARCHAR(255), score INT(255))")

def ins(sid,score):
    sql = "INSERT INTO customers (name, score) VALUES (%i, %i)"
    val = (sid, score)
    mycursor.execute(sql, val)
    mydb.commit()