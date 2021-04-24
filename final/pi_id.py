import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore
import datetime
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

def initial():
    #add email from bluetooth 
    dic = db.collection("Piid").document('1').get().to_dict()
    email = dic['email']
    password  = dic['password']
    print("Log in...")
    uid = "0"
    try:
        login = auth.sign_in_with_email_and_password(email, password)
              
        uid = login['localId']
        invalid = True
    except Exception as e:
        print(e)
        invalid = False
    return uid,invalid

def update(user_id,status):
    date_object = datetime.date.today()
    if status != False:
    #print(date_object)
        vitals_user = db.collection('users').document(user_id).collection('vitals').document(u''.join(str(date_object)))
        vitals_user.set({u'foo.now': firestore.SERVER_TIMESTAMP,u'spo2': u'98%' , u'hemoglobin': u'12.2%' , u'heartrate': 23})
        print("done updating")