############## STTP on IoT & MicroPython ############################
# Author:- Rutvik Mehta                                             
#Title:-   Reading Data from thingspeak and ploting using matplotlib
#E-mail:- rutvik.mehta1990@gmail.com                      
#####################################################################
import matplotlib.pyplot as plt
import urllib.request as ur
import json

response_obj = ur.urlopen('READ_URL_FROM_THINGSPEAK_ACCOUNT')
#print(type(response_obj))
data = response_obj.read()

json_data = json.loads(data)
print (json.dumps(json_data, indent=4))
feeds = json_data["feeds"]
#print(feeds)
alltemp = []
for entry in feeds:
    if entry['field1'] == "":
        continue
    else:
        alltemp.append(float(entry['field1']))
#print(alltemp)
points = list(range(len(alltemp)))
print(points)
plt.plot(points,alltemp,label = "thing speak")
plt.title("IoT Workshop")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.legend()
plt.grid(True, color =  'k')
plt.show()
#data_json = json.loads(str(response_obj))

