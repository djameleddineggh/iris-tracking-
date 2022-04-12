import network
import time

class wifi:
    def __init__(self):
        self.WIFI_SSID = 'YOUR SSID'
        self.WIFI_PASS = 'YOUR WIFI PASSWORD'
    def connect(self):
        print("Connecting to WiFi network '{}'".format(self.WIFI_SSID))
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)
        self.wifi.connect(self.WIFI_SSID, self.WIFI_PASS)
        host=self.wifi.ifconfig()[0]
        return host
    def setwifi_ssid(self,WIFI_SSID):
       self.WIFI_SSID=WIFI_SSID
    def setWIFI_PASS(self,WIFI_PASS):
       self.WIFI_PASS=WIFI_PASS
