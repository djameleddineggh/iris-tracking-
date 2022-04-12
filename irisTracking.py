import facemesh as fm
from detectface import facedetector
import cv2
import numpy as np
from socket import *
import math

def distance(p1 , p2 ) :
    dist = int ( math.hypot ( p1 [ 0 ] - p2 [ 0 ] , p1 [ 1 ] - p2 [ 1 ] ) )
    cntrx , cntry = (p1 [ 0 ] + p2 [ 0 ]) // 2 , (p1 [ 1 ] + p2 [ 1 ]) // 2
    return dist , [ cntrx , cntry ]

def process(eye,threshold=19):
    eye1 = cv2.cvtColor ( eye , cv2.COLOR_BGR2GRAY )
    _ , th1 = cv2.threshold ( eye1 , threshold , 255 , cv2.THRESH_BINARY_INV )
    th1 = cv2.GaussianBlur ( th1 , (5 , 5) , 5 )
    th1 = cv2.morphologyEx ( th1 , cv2.MORPH_OPEN , kernel )
    contours , _ = cv2.findContours ( th1 , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE )
    cnt = max ( contours , key = lambda x : cv2.contourArea ( x ) )
    (x , y) , radius = cv2.minEnclosingCircle ( cnt )
    dist = distance (  m[0][27] [ 1 ] ,m [ 0 ] [ 23 ][1] )
    if 5 < radius < 15 and dist[0] > 24 :
      cv2.circle ( img1 , (int ( x ) , int ( y )) , color = (0 , 0 , 255) , radius = int ( radius ) , thickness = 2 )
      data = 'on'
    else :
      data = 'off'
    data_send = data.encode ( 'utf-8' )
    print(data)
    try :
       UDPSock.sendto ( data_send , addr )   # send the data of a single eye-blink
    except :
        pass


addr = ('',15000)   # put the address for esp8266 connection
UDPSock = socket(AF_INET, SOCK_DGRAM)
cap = cv2.VideoCapture ( 1 )
d=facedetector()
mesh=fm.Meshdetect (nbr_face = 1,r=2 )
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
while True:
    _, img = cap.read ()
    img = cv2.resize ( cv2.flip ( img , 1 ) , (1080 , 780) )
    img1=img2=img.copy()
    img,bbx,rk = d.detect_face ( img)
    img , m = mesh.findfacemesh ( img)
    if len ( m ) != 0 :
       cv2.circle(img,(rk[0][0]-13,rk[0][1]+5),color= (0 , 0 , 255) ,radius = 17 ,thickness = -1)
       hsv = cv2.cvtColor ( img , cv2.COLOR_BGR2HSV )
       mask = cv2.inRange ( hsv , (0 , 255 , 100) , (0 ,255 , 255) )
       maskwhsv = cv2.bitwise_and ( img , img , mask = mask)
       grayimg= cv2.cvtColor ( maskwhsv, cv2.COLOR_BGR2GRAY )
       _ , th = cv2.threshold ( mask , 50 , 255 , cv2.THRESH_BINARY)
       eye= cv2.bitwise_and( img2 , img2 , mask = th)
       eye[th==0]=(255,255,255)
       try:
          process(eye)
       except:
        try:
          process ( eye,threshold=30 )
        except:
         pass

    cv2.imshow ( "Image" , img1 )
    if cv2.waitKey ( 1 ) == ord ( " " ) :
       break
cap.release ( )
cv2.destroyAllWindows ( )