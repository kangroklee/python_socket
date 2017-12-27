#This is a socket chat client program.

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter IP address of server: ")
#host = '192.168.0.36'
port = int(input("Enter port of the server: "))
#port = 8888

s.connect((host, port))

#Chat part
for x in range(2):
    servermsg = s.recv(1024).decode()
    print(servermsg)

while True:
    response = input("> ")
    try:
        #Set the whole string
        #s.sendall(bytes(response, 'utf-8'))
        s.send(response.encode())
    except socket.error:
        #Send failed
        print ("Connection unstable.\n Dropping connection in 3s.")
        time.sleep(3)
        s.close
        sys.exit()

    print("Sent.")

    #servermsg = s.recvfrom(1024)
    servermsg = s.recv(1024).decode()
    #servermsg.decode('utf-8')
    print("Server: ",str(servermsg))
    print("\n")
