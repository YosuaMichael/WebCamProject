import socket
import cv2
import Image
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import StringIO
import time

def main():
	#initialize socket
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#This creates socket

	#initialize camera capture
	vc = cv2.VideoCapture(0)
	vc.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320);
	vc.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240);
	
	#run camera capture
	if vc.isOpened(): # try to get the first frame
		rval, frame = vc.read()
	else:
		rval = False

	client_socket.connect(('192.168.1.19', 50007))
	#client_socket.connect(('127.0.0.1', 50007))
	ct = 1
	while rval:
		rval, frame = vc.read()
		cv2.imwrite('temp.png', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 9])
		f = open('temp.png', 'rb')
		print 'Get image number' + str(ct) 
		
		#send data to server
		data = f.read()
		print len(data)
		client_socket.send(str(len(data)))
		client_socket.recv(1024)
		print 'test'
		client_socket.send(data)
		#client_socket.send(b'Hello world')
		recv_data = client_socket.recv(4096)
		print "Message number " + recv_data + " received."
		
		ct += 1
		
		#escape key
		key = cv2.waitKey(20)
		if key == 27: # exit on ESC
			break
	
	client_socket.close()
 
if __name__ == '__main__':
	main()