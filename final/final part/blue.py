import bluetooth
import maxsensor

class blecomm:
    
    def __init__(self):
        #this step will intialize the bluetooth and wait till its connected
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock = server_sock
        server_sock.bind(("", 1))
        server_sock.listen(1)
        print("Waiting for connection on RFCOMM channel", 1)
        client, address = server_sock.accept()
        print("Connected To", address)
        print("Client:", client)
        self.client = client
        self.address = address
    

    def recivedata(self):
    #to recive data from the bluetooth 
        try:
            data = self.client.recv(1024)
            data = data.rstrip().lstrip()
            data = str(data,"utf-8")
            return data
    
        except OSError:
            return "got error"
    
    def senddata(self,data):
        #to send data from bluetooth 
        try:
            
            self.client.send(data)
            return "sent"
        except Exception as e:
            return "error" + e
        
    def close(self):
        #close the bluetooth connection 
        self.client.close()
        self.server_sock.close()
        print("All done.")
    
class maxsens:
    def __init__(self):
        init_max = maxsensor.MAX30102()# sensor initialization
        self.init_max = init_max
        
    def readval(self):
        #to read value from the sensor 
        import hrcal1
        print("started")
        red, ir = self.init_max.read_sequential()
        hr,_,spo2,_=  hrcal1.calc_hr_and_spo2(ir[:200],red[:200])
        #print(hr,round(spo2,2))
        return hr,round(spo2,2)
        