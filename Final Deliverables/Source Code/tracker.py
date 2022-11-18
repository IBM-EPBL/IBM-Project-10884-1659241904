import json
import wiotp.sdk.device
import time


myConfig = {
    "identity": {
        "orgId": "43j9ja",
        "typeId": "NODE",
        "deviceId": "1501"
    },
    "auth": {
        "token": "012345678"
        }
}

        
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name= "Sowmiya"
    #in area location

    #latitude=9.262304
    #longitude= 78.875537

    #out area location

    latitude= 20.3452
    longitude= 78.5488783
    mydata={'name': name, 'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
    print("Data published to IBM IoT platform: ",mydata)
    time.sleep(20)


client.disconnect()
