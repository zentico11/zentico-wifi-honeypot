Zentico Wi-Fi Honeypot Tool

This tool creates a fake Wi-Fi network and lists connected devices, allowing you to kick or ban them.

Requirements:
- Linux (Debian-based)
- Python 3
- Hostapd, Dnsmasq, Iptables
- Sudo/Root Privileges
- Ap Supported Wi-fi Adaptor 

Installation:
1. Install required packages:
   sudo apt install hostapd dnsmasq

2. Configure the wireless interface:
   sudo ip link set wlan0 down
   sudo ip addr add 192.168.150.1/24 dev wlan0
   sudo ip link set wlan0 up

3. Start the tool:
   sudo python3 main.py

Warning: Use only on your own network or in legal testing environments.

