import socket
import mysql.connector
from mysql.connector import Error
from io import BytesIO

# MySQL Database Configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'socket'
}

# Function to store file data in MySQL
def store_file_in_database(file_data):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Assuming you have a table named 'files' with columns 'id' and 'file_data'
        cursor.execute("INSERT INTO files (file_data) VALUES (%s)", (file_data,))
        connection.commit()
        print("File stored in the database successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Server Configuration
# Change the port number
server_address = ('localhost', 12345)
buffer_size = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(server_address)
    server_socket.listen()

    print("Server listening on", server_address)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from", client_address)

        file_data = BytesIO()

        while True:
            data = client_socket.recv(buffer_size)
            if not data:
                break
            file_data.write(data)

        store_file_in_database(file_data.getvalue())

        file_data.close()  # Close BytesIO to free up resources
        client_socket.close()
        print("Connection closed")
