import socket
import time
#import cv2

def num():
    num.counter = (num.counter + 1) % 30
    return num.counter
num.counter = 0

def main():
    #initializing socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    server_socket.bind(('', 50007))

    print "UDPServer Waiting for client on port 6666"
    
    #start waiting for data
    
    ct = 1
    
    server_socket.listen(1)
    conn, address = server_socket.accept()
    while True:
        
        length = int(conn.recv(1024))
        conn.send('a')
        
        print length
        data = b''
        while length>0:
            dataFromClient = conn.recv(length)
            data += dataFromClient
            length -= len(dataFromClient)
            print str(len(dataFromClient)) + ' ' + str(length)
        
        #receive data
        temp = num()
        f = open('data/temp'+str(temp)+'.png', 'wb')
        f.write(data)
        f.close()
        f = open('data/temp.txt', 'w')
        f.write(str(temp))
        f.close()
        
        #respond to client
        epochTime = str(time.time())
        print "Obtaining data number " + str(ct) + " at time " + epochTime + " from " + str(address) + "."
        conn.send(str(ct)+',')
        ct += 1
        
    
    conn.close()

if __name__ == '__main__':
    main()
