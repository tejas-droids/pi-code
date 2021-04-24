import math as m
import maxsensor 
import hrcal
import time
import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore
import datetime
import bluetooth
date_object = datetime.date.today()
config = {
  "apiKey": "AIzaSyDOwpfUu8V724gseECDjf03YMiZkqKdDc4",
  "authDomain": "teamtechnocrats-def72.firebaseapp.com",
  "databaseURL": "https://teamtechnocrats-def72.firebaseio.com",
  "storageBucket": "teamtechnocrats-def72.com",
  "serviceAccount": "serviceAccountCredentials.json"
}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
cred = credentials.Certificate("serviceAccountCredentials.json")
firebase_admin.initialize_app(cred)
# initialisatiing Database
db = firestore.client()
time.sleep(2)


#spo2_pre_defined =[100,100,100,IndexError100,99,99,99,99,99,99,98,98,98,98,\
 #                                            98,97,97,97,97,97,97,96,96,96,96,96,96,95,95,\
   #                                          95,95,95,95,94,94,94,94,94,93,93,93,93,93]
h = maxsensor.MAX30102()# sensor initialization
def login(email,password):
    print("Log in...")
   
    uid = "0"
    try:
        login = auth.sign_in_with_email_and_password(email, password)
              
        uid = login['localId']
        
        invalid = True
    except:
        print("try again")
        invalid = False
    return uid,invalid
time.sleep(5)
db = firestore.client()
doc = db.collection("Piid").document('69').get().to_dict()
user_id,status = login(doc['email'],doc['password'])
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", 1))
server_sock.listen(1)
print("Waiting for connection on RFCOMM channel", 1)
client, address = server_sock.accept()
print("Connected To", address)
print("Client:", client)
try:
    data = client.recv(1024)
    data =data.rstrip().lstrip()
    data = str(data,"utf-8")
    if data.upper() == '1':
        print("started reading")
        red, ir = h.read_sequential()
        heart_rate,_,spo2,_,irac_square,redac_square,ratio,samples =  hrcal.calc_hr_and_spo2(ir[:200],red[:200])
        ratio.sort()
        try:
            ratio_len = ratio[int(len(ratio)/2)]
            official_spo2 = 104 -(17 * ratio_len)
            hemoglobin = 14.937 -(3*ratio_len)
        
            if status != False:
    #print(date_object)
                vitals_user = db.collection('users').document(user_id).collection(u'vitals').document(u'{}'.format(date_object))
                vitals_user.set({u'date': str(date_object),u'spo2': u'{}%'.format(round(official_spo2,2)) , u'hemoglobin': u'{}g/dl'.format(round(hemoglobin,2)), u'heartrate': u'{}bpm'.format(heart_rate)})
                official_spo2 = 104 -(17 * ratio_len)
                hemoglobin = 14.937 -(3*ratio_len)
                print("heart rate :",heart_rate,"Bpm","\n","test  hemoglobin :",round(hemoglobin,2),"g/dl","\n","spo2:",round(official_spo2,2),"%","\n",)   
                #client.send("{} %\r\n ".format(str(round(official_spo2,2 ))))
                client.send("heart rate {}bpm \r\n ".format(str(heart_rate)))
                #client.send("hemoglobin {} g/dl \r\n ".format(str(round(hemoglobin,2))))
                time.sleep(30)
                client.close()
                server_sock.close()
                print("All done.")
        except IndexError:
            print("faild try again")


except OSError:
    pass

print("Disconnected.")
time.sleep(3)
client.close()
server_sock.close()
print("All done.")






#print("heart rate :",heart_rate,"Bpm","\n","test  hemoglobin :",round(hemoglobin,2),"g/dl","\n","spo2:",round(official_spo2,2),"%","\n",)
    #print("oxygen level git formula:",spo2,"%")

    #print(red,ir)# get LEDs readings
    #f =open("data.txt","w")
    #f.write("["+str(red)+","+str(ir)+"]")
    #f.close()
    #d.DataFrame(data=zip(red,ir),columns=["red","ir"]).to_csv("data.csv")
    #print(red,ir)

    #print(ratio,ratio_len)
    
    #ratio_len = sum(ratio[:-3])/len(ratio[:-3])
        
    #print("oxygen level git formula:",spo2,"%")
    #print("spo2:",round(official_spo2,2),"%")
 #   print("test  hemoglobin :",round(hemoglobin,2),"g/dl")
    
        
