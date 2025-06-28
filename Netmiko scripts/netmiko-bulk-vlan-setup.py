from netmiko import ConnectHandler

# For this script to work, SSH needs to be enabled on the network devices.

# Device connection parameters
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'Princeton',
    'password': '<enter your password>',
}

# Connect to switch
net_connect = ConnectHandler(**iosv_l2)

# Show current interface status
output = net_connect.send_command('show ip int brief')
print(output)

# Configure loopback interface
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

# Create VLANs 2-20
for n in range(2,21):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)

# Close connection
net_connect.disconnect()
