import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Amiandami@22'
    )

cursorObject = dataBase.cursor()

cursorObject.execute("Create DATABASE DCRMDB")

print("Done all!")