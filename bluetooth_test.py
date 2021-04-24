import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", 1))
server_sock.listen(1)



print("Waiting for connection on RFCOMM channel", 1)
client, address = server_sock.accept()
print("Connected To", address)
print("Client:", client)


try:
    while True:
        data = client.recv(1024)
        data =data.rstrip().lstrip()
        data = str(data,"utf-8")
        print(data)
        if data.upper() == 'A':
            client.send("spo2")
        if data.upper() == 'END':
            client.send("end")
            client.close()
            server_sock.close()
            print("All done.")
       
except OSError:
    pass

print("Disconnected.")

client.close()
server_sock.close()
print("All done.")