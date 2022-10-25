import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Simple local IP finder v1.0 by kict0")
print("The name of your computer is: " + hostname)
print("Your local IP is: " + ip)
