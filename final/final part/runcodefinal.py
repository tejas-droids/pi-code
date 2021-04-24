#from pi_id import *
from blue import blecomm
from blue import maxsens

#
maxsensor = maxsens()
blue= blecomm()


while True:
    data = blue.recivedata()
    if data.upper() == "1":
        hr,spo2 = maxsensor.readval()
        error = blue.senddata("{}BPM".format(hr))
        print(hr)
    if data.upper() == "2":
        hr,spo2 = maxsensor.readval()
        error = blue.senddata("{}% ".format(spo2))
        print(spo2)
    if data.upper() == 'END':
        blue.close()
        break

