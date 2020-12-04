# 2. Prompt a user to enter in an IP address from standard input. Read the IP address in
# and break it up into its octets. Print out the octets in decimal, binary, and hex.

ip_addr = input("Enter an IP address: ")
ip_addr = ip_addr.split(".")
print("Octet 1 - " + ip_addr[0] + " Binary: " + bin(int(ip_addr[0])) + " Hex: " + hex(int(ip_addr[0])))
print("Octet 2 - " + ip_addr[1] + " Binary: " + bin(int(ip_addr[1])) + " Hex: " + hex(int(ip_addr[1])))
print("Octet 3 - " + ip_addr[2] + " Binary: " + bin(int(ip_addr[2])) + " Hex: " + hex(int(ip_addr[2])))
print("Octet 4 - " + ip_addr[3] + " Binary: " + bin(int(ip_addr[3])) + " Hex: " + hex(int(ip_addr[3])))
