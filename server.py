import socket
import sys

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# --- 2 Bind socket ---
try:
    my_socket.bind(("192.168.0.126", 80))
except socket.error:
    print("Failed to bind")
    sys.exit()
# --- 3 Listen for a connection ---
my_socket.listen(5)

# --- 4 Accept connection ---
while True:
    client_connection, client_address = my_socket.accept()
    # --- 5 Receive data ---
    data = client_connection.recv(1024)
    if not data:
        break
    print ("Got a request!")
    print (data)

    # --- 6 Send response ---
    http_response = b"\HTTP/1.1 200 OK "
    client_connection.sendall(http_response)

client_connection.close()
my_socket.close()
