import socket
import sys  
host = "" # connects to the host and the port of the server
port = 12348 #
# create socket
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# creat a TCP socket refer to IPv4 
  print("Socket is created")
except socket.error as ms: #catch for error in creating of socket
  print("Failed to create socket" + ms)
  sys.exit()
if True:
 # Connect to remote server
  s.connect((host , port))#establishes a connection with the server.
  print("You are connected")
  # Send data to remote server
try:
  while True: 
    print("Sending data to server")
    messenge = input(">>>")
    try:
      s.sendall(messenge.encode("UTF-8"))#encode data 
    except s.error:
      print ('Send failed')
      sys.exit()
    # Receive data
      print("Receive data from server")
      data = s.recv(4096)# buffer size
      data = data.decode("UTF-8")#decode and print data from the server
      print (">>>" + data)
    if messenge == "exit":
      print("Connection lost")
      s.close()
except KeyboardInterrupt:
    print("conncetion lost")
    s.shutdown(1)
    s.close()         