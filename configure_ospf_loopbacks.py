# Original script template is from telnetlib - https://docs.python.org/3.12/library/telnetlib.html

# Import required libraries
import getpass
import telnetlib
import time

# Defines the target network host and get user credentials
HOST = "192.168.122.71"
user = input("Enter your telnet  username: ")
password = getpass.getpass()

# Establish a Telnet connection to the device
tn = telnetlib.Telnet(HOST)

# Read the prompts and send the username and password
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Enter enable mode and send configuration commands
tn.write(b"enable\n")
tn.write(b"<type your password in here>\n")
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")

# Wait for commands to process, then save the configuration and exit
time.sleep(5)
tn.write(b"wr mem\n")
tn.write(b"exit\n")

# Print the entire session output to the console
print(tn.read_all().decode('ascii'))
