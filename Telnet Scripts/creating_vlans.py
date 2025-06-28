# Original script template is from telnetlib - https://docs.python.org/3.12/library/telnetlib.html

# Import required libraries
import getpass
import telnetlib
import time

# Defines the target network host (which is switch 1) and gets user credentials
HOST = "192.168.122.72"
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
tn.write(b"<enter password here>\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN_5\n")
tn.write(b"end\n")

# Wait for commands to process, then save the configuration and exit
time.sleep(5)
tn.write(b"wr mem\n")
tn.write(b"exit\n")

# Print the entire session output to the console
print(tn.read_all().decode('ascii'))
