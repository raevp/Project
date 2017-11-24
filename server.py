import socket
import sys
host = "127.0.0.1"  # IP addres of the server.
port = 12348 # port of the server.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creat a TCP socket refer to IPv4 
print('# Socket created')
# Create socket on port
try:
  s.bind((host, port)) # used to associate the socket with the server address.
except socket.error as ms: #catch for error.
  print("falied" + str(ms))
  sys.exit()
if True:
  print('# Socket bind complete')
s.listen(1) # turn the socket into server mode.
print('# Socket now listening')
# Wait for client
conn, addr = s.accept() # returns an open connection between the server and client
if True:
   print('# Connected to ' + addr[0] + ':' + str(addr[1]))
# Receive data from client
try:
  while True:
    data = conn.recv(4096) # buffer size 
    data = data.decode("UTF-8") # decode data
    print("User>>>" + data )
    if True:
      print ("Sending data to User")
      conn.send(data.encode("UTF-8")) # encode data and send to client
  conn.close()   
except KeyboardInterrupt: # catch for Ctrl+C 
    print("Conncetion lost")
    conn.shutdown(1)
    conn.close()    