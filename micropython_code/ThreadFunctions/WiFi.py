import network
from lib.nextion import nextion
import os
import machine
import time

WiFi = network.WLAN(network.STA_IF)
WiFi.active(1)

display = nextion(12, 13, 9600)

def connect():
        response = None
        while response is None:
            response = display.read()
        r_ssid = bytearray(response).decode("ASCII")
        r_ssid = str(r_ssid).replace("b'", "")
        r_ssid = str(r_ssid).replace("'", "")
        print("Received ssid data. SSID: " + r_ssid)
        response = None
        while response is None:
            response = display.read()
        r_password = bytearray(response).decode("ASCII")
        r_password = str(r_password).replace("b'", "")
        r_password = str(r_password).replace("'", "")
        print("Received password data. Password: " + r_password)
        print("ssid: " + r_ssid + " password: " + r_password)
        print("WiFi Connect...")
        
        WiFi.active(1)
        WiFi.connect(r_ssid, r_password)
        while not WiFi.isconnected():
            pass
        print('network config:', WiFi.ifconfig())
        print("Connected to WiFi Successful")
#         WiFi.active(1)
#         wifis = WiFi.scan()
#         WiFi.scan()
#         files = os.listdir("wifi")
#     
#         i = 0
#         wififound = 0
#         while i <= len(wifis) - 1:
#             b_ssid = wifis[i][0]
#             ssid = str(b_ssid)
#             ssid = ssid.replace("b", "")
#             ssid = ssid.replace("'", "")
#             print(ssid)
#             b_bssid = wifis[i][1]
#             bssid = str(b_bssid)
#             bssid = bssid.replace("b", "")
#             bssid = bssid.replace("'", "")
#             print(bssid)
#             cnt = 0
#             while cnt <= len(files) - 1:
#                 if files[cnt] == str(ssid):
#                     path = "wifi/";
#                     path += files[cnt]
#                     wififile = open(path)
#                     fcontent = wififile.read()
#                     print(fcontent)
#                     wififile.close()
#                     wifidata = fcontent.split("|||")
#                     print(wifidata[0].replace("//", "/"))
#                     if wifidata[0] == bssid:
#                         print("Connect to WiFi...")
#                         wififound = 1
#                         break
#                 cnt += 1
#                 print(cnt)
#             i += 1
#             if wififound == 1:
#                 try:
#                     print("WiFi Connect...")
#                     if not WiFi.isconnected():
#                         WiFi.active(True)
#                         print("ssid: " + ssid + " password: " + wifidata[1])
#                         WiFi.connect(ssid, wifidata[1])
#                         while not WiFi.isconnected():
#                             pass
#                         return wififound
#                         print('network config:', WiFi.ifconfig())
#                     
#                     break
#                 except:
#                     print("Error at Block 364-373")
#                     sys.exit()
# 
#         wififile = open("wifi/" + r_ssid, "w")
#         wififile.write(bssid + "|||" + r_password)
#         wififile.close()
#         del wififile

        time.sleep(1)
        print(display.page("Home"))
