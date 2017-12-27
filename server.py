#This is another iteration of NightlyProj.py
#send method changed.

import socket
import sys
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created.")
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ("Bind failed.")
    sys.exit()
     
print ('Socket bind complete.')
 
#Start listening on socket
s.listen(3)
print ('Socket initialized.\nSocket now listening...')
 
#now keep talking with the client
conn, addr = s.accept()
print ('Connected with ' + addr[0] + ':' + str(addr[1]))
print('\n')
#s.close()

#Send connection header
#header = "You are connected to: ", socket.gethostname()
try :
    header1 = "You are connected to: %s" % socket.gethostname()
    conn.send(header1.encode())
    #conn.sendto(bytes("Enter anything to start chat...\n", 'utf-8'), addr)
    header2 = "Enter anything to start chat...\n"
    conn.send(header2.encode())
except socket.error:
    #Send failed
    print ("Connection unstable.\n Dropping connection in 3s.")
    time.sleep(3)
    s.close
    sys.exit()
        
#Now keep talking with the client (RECEIVE input first!)
while True:
    #clientmsg, temp = conn.recvfrom(1024)
    clientmsg = conn.recv(1024).decode()
    #clientmsg.decode('utf-8')
    #print("Incoming: ", clientmsg)
    print("Incoming: ", str(clientmsg))

    response = input("Reply: ")
    try:
        #Set the whole string
        #conn.sendto(bytes(response, 'utf-8'), addr)
        conn.send(response.encode())
    except socket.error:
        #Send failed
        print ("Connection unstable.\n Dropping connection in 3s.")
        time.sleep(3)
        s.close
        sys.exit()

    print ("Sent.\n")



"""
#Previous version - no encoding

#Connection header
hostip = socket.gethostname()
header = "You are connected to %s" % str(hostip)

try :
    #Set the whole string
    s.sendall(header)
except socket.error:
    #Send failed
    print ("Connection unstable.\n Dropping connection in 3s.")
    time.sleep(3)
    s.close
    sys.exit()
 
print ("\nSent.\n")
 
#Now receive data
clientmsg = s.recv(4096)
print("Incoming: ", clientmsg)

response = input("Reply: ")
try :
    #Set the whole string
    s.sendall(response)
except socket.error:
    #Send failed
    print ("Connection unstable.\n Dropping connection in 3s.")
    time.sleep(3)
    s.close
    sys.exit()

print ("\nSent.\n")
"""
