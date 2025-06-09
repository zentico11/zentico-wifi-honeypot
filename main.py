import tkinter as tk
from tkinter import messagebox
import subprocess
import threading

banned_macs = set()

def start_ap():
    subprocess.call(['sudo', 'hostapd', 'config/hostapd.conf'])

def start_dhcp():
    subprocess.call(['sudo', 'dnsmasq', '-C', 'config/dnsmasq.conf'])

def launch_ap():
    threading.Thread(target=start_ap).start()
    threading.Thread(target=start_dhcp).start()
    messagebox.showinfo("Started", "Started Fake Wifi Network!")

def monitor_clients():
    clients.delete(0, tk.END)
    result = subprocess.check_output("arp -a", shell=True).decode()
    for line in result.splitlines():
        if 'wlan0' in line:
            parts = line.split()
            ip = parts[0]
            mac = parts[1]
            if mac not in banned_macs:
                clients.insert(tk.END, f"{mac} ({ip})")

def kick_selected():
    selected = clients.get(clients.curselection())
    mac = selected.split()[0]
    subprocess.call(f"sudo iptables -A INPUT -m mac --mac-source {mac} -j DROP", shell=True)
    banned_macs.add(mac)
    messagebox.showinfo("Kicked!", f"{mac} Banned!")

root = tk.Tk()
root.title("Zentico Wi-Fi Honeypot Control Panel")

tk.Button(root, text="Start Wifi Network", command=launch_ap).pack(pady=5)
tk.Button(root, text="Scan Devices", command=monitor_clients).pack(pady=5)

clients = tk.Listbox(root, width=50)
clients.pack(pady=10)

tk.Button(root, text="Ban Chosen Device", command=kick_selected).pack(pady=5)

root.mainloop()
