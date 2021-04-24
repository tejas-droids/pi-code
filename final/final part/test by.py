from bluetooth import *
port = 1
backlog = 1
host=''
server_sock=BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try:
    server_sock.bind((host,port))
    print("Bluetooth Binding Completed")
except:
    print("Bluetooth Binding Failed")

server_sock.listen (backlog)
client_sock , client_info = server_sock.accept ( )
print("Accepted connection from " , client_info[0])
try:
    while True:
        data = client_sock.recv(1024)
        data =data.rstrip().lstrip()
        data = str(data,"utf-8")
        print(data)
        if str(data) == 'A':
            send_data = "Light On\r\n "
        server_sock.send(send_data)
    
except:
    client_sock.close ( )
    server_sock . close ()
