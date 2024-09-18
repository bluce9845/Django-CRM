import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'rizki.,1927'
)

cursoObject = dataBase.cursor()

cursoObject.execute("CREATE DATABASE cosmos") 

print("All Done!")