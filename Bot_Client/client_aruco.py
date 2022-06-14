import base64
import json                    
import cv2
import requests
from imutils.video import VideoStream
import mover
import time
from time import sleep
from weed_helper import check
from sprayer import spray
vs = VideoStream(usePiCamera=False).start()
while True:
    frame=vs.read()
    api = 'http://192.168.191.198:5000/aruco'
    image_file = 'send.jpg'
    cv2.imwrite(image_file,frame)
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    payload = json.dumps({"image": im_b64, "other_key": "value"})
    response = requests.post(api, data=payload, headers=headers)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord("q"):
        break
    
    try:
        data = response.json()     
        print(data)
        output,t1=data["output"],data["timeout"]
        mover.receiver(data["output"])
        time.sleep(t1)
        mover.receiver("5")
        
        print("Checking for Weed")
        check()
        sleep(2)
        
    except requests.exceptions.RequestException:
            print(response.text)




