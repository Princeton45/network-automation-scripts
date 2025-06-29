"""
Script to retrieve device facts from a Cisco IOS device using NAPALM
This script connects to a network device and displays basic information
"""
import json
from napalm import get_network_driver

# Get the appropriate driver for Cisco IOS devices
driver = get_network_driver('ios')

# Creates a device connection object with IP address, username, and password
iosvl2 = driver('192.168.122.72', 'Princeton', '<enter your switch password here>')

# Open the connection to the device
iosvl2.open()

# Retrieve device facts (hostname, model, serial, OS version, uptime, etc.)
ios_output = iosvl2.get_facts()

# Display the retrieved device information
print (json.dumps(ios_output, indent=4))

