from scapy.all import *
import ipaddress
import os
import sys

if os.name != "nt" and os.geteuid() != 0:
    print("You need to run this script as root!")
    sys.exit()

while True:
    try:
        ipA = input("Enter IP address: ")
        ipB = ipaddress.ip_address(ipA)
        break
    except ipaddress.AddressValueError:
        print("Invalid IP address!")

try:
    ping = sr1(IP(dst=str(ipB))/ICMP(), timeout=3, verbose=0)
    if ping:
        print(f'Time To Live (TTL): {ping[IP].ttl}')
        ping.show()
    else:
        print("No response received.")
except PermissionError:
    print("You need to run this script as an administrator/root user!")
except KeyboardInterrupt:
    print("\nScript interrupted by user.")
    sys.exit()
except Exception as e:
    print(f"An error occurred: {e}")