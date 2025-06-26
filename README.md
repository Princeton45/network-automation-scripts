The scripts are being ran against my GNS3 network topology:

This network topology illustrates a small, managed network designed for network automation tasks.

![image](https://github.com/user-attachments/assets/1a84e80e-c4e2-45fb-9bb5-5efcdaa8e517)


At the center of the topology is Switch1, which serves as the primary access and distribution point. Connected to this switch are three distinct elements:

NetworkAutomation-1: This is where the scripts are being ran from. It is a Ubuntu Linux server, connected via its eth0 interface to port e0 of Switch1. This server acts as the management station from which automation scripts are run.

NAT1 Cloud: Representing a connection to an external network (likely the internet), the NAT cloud is linked to port e1 of Switch1. This provides outside connectivity for the management server.

Core Network Devices: The internal network infrastructure begins with device S1 (likely a multilayer switch or firewall), which is connected to port e2 of Switch1 via its own Gi0/0 port. This device, in turn, connects from its Gi0/1 port to the R1 router's Gi0/0 port.



