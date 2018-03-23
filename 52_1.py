import socket


s = socket.socket()
host = socket.gethostname()
port = 12222

s.connect((host, port))
print( 'Connected to', host)

# Halts
print ('[Waiting for response...]')
data = s.recv(1024).decode('utf-8')
data_dict = eval(data)
ymd = str(data_dict["curtime"]).split()[0]
time = str(data_dict["curtime"]).split()[1]
print ymd
print time

s.close()
