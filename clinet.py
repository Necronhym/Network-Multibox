import socket
import pyautogui

host = str(input("Input Server IP address: "))
port = int(input("Input port number: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
	try:
		s.connect((host, 1234))
		break
	except:
		continue
msg = s.recv(1024).decode()
print(msg)
while True:
	msg = s.recv(1024).decode()
	if (msg.find("Key")>0):
		st = msg.find('Key') +4
		if msg.find("release"):
			pyautogui.keyDown(msg[st:])
		if msg.find("press"):
			pyautogui.keyUp(msg[st:])
	else:
		st = msg.find('\'') +1
		if msg.find("release"):
			pyautogui.keyDown(msg[st:-1])
		if msg.find("press"):
			pyautogui.keyUp(msg[st:-1])
