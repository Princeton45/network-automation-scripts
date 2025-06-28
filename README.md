# GNS3 Network Automation Lab

This repository contains Python scripts designed to automate the configuration of network devices within a GNS3 lab environment. The primary goal is to demonstrate how to programmatically connect to devices and deploy standard configurations.

## Network Topology

The scripts are ran against the GNS3 network topology shown below. It features a dedicated management server that configures the internal network devices.

![Network Topology Diagram](https://github.com/user-attachments/assets/1a84e80e-c4e2-45fb-9bb5-5efcdaa8e517)

### Key Components

*   **NetworkAutomation-1**: This is an Ubuntu Linux server imported from the GNS3 Network Automation appliance, where the Python scripts are executed. It connects via its `eth0` interface to the switch and acts as the central management station.

*   **Switch1**: A standard Layer 2 switch that serves as the primary access point, linking all network segments together.

*   **NAT1 Cloud**: This allows the `NetworkAutomation-1` server to access the internet and download packages or connect to outside resources.

*   **Core Network Devices**: The internal infrastructure that is the target of the automation scripts.
    *   **S1**: A Layer 3 switch that connects `Switch1` to the rest of the internal network.
    *   **R1**: A router that serves as the core routing device for this lab.
