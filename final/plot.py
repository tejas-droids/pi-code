import json
from ast import literal_eval

f= open("data1.txt","r")
data=f.read()
f.close()
with open("data1.json","r") as output:
    data = json.loads(output)
print(data)