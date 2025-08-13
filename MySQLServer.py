import mysql.connector
from mysql.connector import errorcode

# Database configuration
DB_HOST = "localhost"
DB_USER = "root"  # Change to your MySQL username
DB_PASSWORD = ""  # Change to your MySQL password
DB_NAME = "alx_book_store"

try:
    # Connect to MySQL server without specifying a database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Create the database if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    
    print(f"Database '{DB_NAME}' created successfully!")
    
except mysql.connector.Error as err:
    # Handle specific error for access denied
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied - Incorrect username or password")
    # Handle other errors
    else:
        print(f"Error: {err.msg}")
    
finally:
    # Close cursor and connection if they exist
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")