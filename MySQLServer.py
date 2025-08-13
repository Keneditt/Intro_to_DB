import subprocess

def create_database():
    # Database configuration
    DB_HOST = "localhost"
    DB_USER = "root"  # Change to your MySQL username
    DB_PASSWORD = ""  # Change to your MySQL password
    DB_NAME = "alx_book_store"
    
    try:
        # Construct the MySQL command
        command = f"mysql -h {DB_HOST} -u {DB_USER} "
        if DB_PASSWORD:
            command += f"-p{DB_PASSWORD} "
        
        command += f"-e 'CREATE DATABASE IF NOT EXISTS {DB_NAME};'"
        
        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if database was created
        if result.returncode == 0:
            print(f"Database '{DB_NAME}' created successfully!")
        else:
            print("Error creating database:", result.stderr)
    
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to execute MySQL command - {e.stderr}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    create_database()