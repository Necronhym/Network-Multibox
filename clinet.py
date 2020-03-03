import socket
import pyautogui

host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 1234))
msg = s.recv(1024).decode()
print(msg)
while True:
	msg = s.recv(1024).decode()
	if msg.find("press") :
                pyautogui.keyDown(msg[-2])
	if msg.find("release") :
		pyautogui.keyUp(msg[-2])
