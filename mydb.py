
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
    
)



corsorObject = dataBase.cursor()


corsorObject.execute("CREATE DATABASE eldero")

print("All Done!")
