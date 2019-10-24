import os
import socket
import time


def change_ip_address():
    # get the connected network adapter name from netsh
    adapter_name_line = os.popen('netsh interface show interface | find "Connected"').read()
    # TODO: parsing of the cmd output seems os and version dependent
    adapter_name_list = adapter_name_line.split()
    network_adapter_name = adapter_name_list[3].strip()  # TODO: is the posision always the same?
    print("network_adapter_name: " + network_adapter_name)

    # default gateway from netsh
    default_gateway_line = os.popen('netsh interface ipv4 show config| findstr "Default.Gateway"').read()
    default_gateway_list = default_gateway_line.split(": ")
    default_gateway = default_gateway_list[1].strip()
    print("default_gateway: " + default_gateway)

    # network subnet mask from ipconfig
    subnet_mask_line = os.popen('ipconfig | findstr "Subnet Mask"').read()
    subnet_mask_list = subnet_mask_line.split(": ")
    subnet_mask = subnet_mask_list[1]
    print("subnet_mask: " + subnet_mask)

    # retrieve the hostname of the local machine
    hostname = socket.gethostname()
    # retrieve the ip
    ip_address = socket.gethostbyname(hostname)
    print("Host Name: " + hostname)
    print("Current IPv4 Address: " + ip_address)

    # get new desired address:
    new_ip_address = input("New desired IP address: ")  # TODO: will need user input validation

    # change the ip address by running a command
    os.system('netsh interface ipv4 set address name="' + network_adapter_name + '" static '
              + new_ip_address + ' ' + subnet_mask + ' ' + default_gateway)
    # timeout to allow ip change
    time.sleep(4)
    ip_address = socket.gethostbyname(hostname)
    print("NEW IP Address is: " + ip_address)

    # revert
    os.system('netsh interface ipv4 set address name="' + network_adapter_name + '" source=dhcp')
    time.sleep(4)
    ip_address = socket.gethostbyname(hostname)
    print("Reverting to DHCP, IP Address is: " + ip_address)


change_ip_address()
