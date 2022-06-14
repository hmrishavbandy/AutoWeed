import cv2
import cv2.aruco as aruco
import numpy as np
import time

def predict(frame):
    
    #frame=cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if len(corners)==0:
        print("Waiting for Marker... <<BOT STOPPED>>")#,end="\r")
        return 5,0.1
        
    if len(corners)>1:
        print("More than one corner detected. Going with the first")#,end="\r")
    c = corners[0][0]
        
    y,x,_=frame.shape
    
    print("Located at ({},{}) ARUCO_ID {} of ({},{})".format(c[:, 0].mean(),c[:, 1].mean(),ids[0],x,y))

    ## First is horizontal. Mid val: 320
    val_h=c[:,0].mean()
    print(val_h)
    if (val_h<=240):
        return 3,0.07
    elif (val_h>=270):
        return 4,0.07
    

    frame=cv2.rectangle(frame, (int(c[0][0]),int(c[0][1])), (int(c[2][0]),int(c[2][1])), (255,255,0), 2)
    
    box_area=np.abs(c[0][0]-c[0][1])*np.abs(c[2][0]-c[2][1])
    frame_area=frame.shape[1]*frame.shape[0]

    if (box_area/frame_area)<=0.5:
        print("\nARUCO too Far {:.4f}. <<Move BOT FWD>>".format(box_area/frame_area))
        print("<<F>>")
        return 2,0.5
        

######################################   
    if ids[0]==[1]:
        print("<<F>>")
        return 2,0.5
        # receiver(2)
    elif ids[0]==[2]:
        print("<<B>>")
        return 1,0.5
        # receiver(1)
    elif ids[0]==[3]:
        print("<<L>>")
        return 3,1
        # receiver(3)
    elif ids[0]==[4]:
        print("<<R>>")
        return 4,1
        # receiver(4)
    else:
        print("Pattern not detected!!")

        # Check.My_Function(1)
        return 5,0.01
    
    # if (box_area/frame_area)>=0.05:
    #     print("\nARUCO too close {:.4f}. <<Move BOT>>".format(box_area/frame_area))
    #     process(id=ids[0])
    #     time.sleep(0.3)
    # return 5