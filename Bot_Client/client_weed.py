import base64
import json                    

import requests
from sprayer import spray
from time import sleep
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (512,512)
camera.start_preview()

while(1):
    
    sleep(2)
    camera.capture('send.jpg')


    api = 'http://192.168.191.198:5000/weed'
    image_file = 'send.jpg'
    
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    payload = json.dumps({"image": im_b64, "other_key": "value"})
    response = requests.post(api, data=payload, headers=headers)
    try:
        out= response.json()
        #print(out)
        data=out["output"]
        bbox=out["dict"]
        frame=out["frame"]
        if sum(bbox)!=0:
            spray(bbox,frame)
        print(data)
        print(bbox)
    except requests.exceptions.RequestException:
            print(response.text)
