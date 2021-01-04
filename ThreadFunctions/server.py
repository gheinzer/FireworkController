import network
try:
  import usocket as socket
except:
  import socket
from ThreadFunctions.DirectLaunch import *
from lib.nextion import nextion
import _thread

display = nextion(12, 13, 9600)

def start_server():
    print("starting server...")
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.active(True)         # activate the interface
    ap.config(essid='FireworkController',password=b"micropython",channel=11,authmode=network.AUTH_WPA_WPA2_PSK)
    while 1:
        if(ap.isconnected()):
            break
    display.cmd("page IPShow")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    print('Web-Server is started.')
    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        display.page("Home")
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        ch1 = request.find('/?ch=1')
        ch2 = request.find('/?ch=2')
        if ch1 == 6:
            _thread.start_new_thread(LAUNCH, ["1"])
        if ch2 == 6:
            _thread.start_new_thread(LAUNCH, ["2"])
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

def web_page():
    html = """<html><head> <title>FireworkController</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>FireworkController WEB</h1><p><a href="/?ch=1"><button class="button">LAUNCH CH1</button></a></p>
    <p><a href="/?ch=2"><button class="button button2">LAUNCH CH2</button></a></p></body></html>"""
    return html
