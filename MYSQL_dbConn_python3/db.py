# Importing File
import mysql.connector
from mysql.connector import Error

# Creating Connection
connection = mysql.connector.connect(
    host='localhost',
    database='one',
    user='admin',
    password='admin@1234'
)

# Error Handling
try:
    # Check connection is sccessfull or not
    if connection.is_connected():
        # SQL Version
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        # Cursor Object 
        cursor = connection.cursor()
        # SLQL Query to execute
        cursor.execute("select database();")

        # Fetch Data from table 
        record = cursor.fetchone()
        print("You're connected to database: ", record)
# Exceptd Error
except Error as e:
    print("Error while connecting to MySQL", e)
# Default Execution
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
