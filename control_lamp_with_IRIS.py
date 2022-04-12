import Connect2esp as c2e
from socket import *
import time
from machine import Pin
lamp= Pin(05, Pin.OUT)
lamp.on()

host=c2e.wifi().connect()
cmp1=cmp2=0
s=8
addr = (host,15000)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print(addr[0],':',addr[1])

while True:
   if UDPSock.recv!=None: 
    (data, addr) = UDPSock.recvfrom(10000)
    data=data.decode('utf-8')
    print ("Received message: " , data)
    #time.sleep(0.15)
    if data=='on':
     cmp1+=1
     if cmp1>s:
      lamp.on()
      cmp1=0
    elif data=='off':
     cmp2+=1
     if cmp2>s:   
      lamp.off()
      cmp2=0
    
UDPSock.close()
os._exit(0)
