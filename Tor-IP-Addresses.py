import requests
import re
import os

try:
    print("Downloading Tor exit addresses list...")
    url = 'https://check.torproject.org/exit-addresses'
    req = requests.get(url, allow_redirects=True)
    open('Tor.txt', 'wb').write(req.content)
except requests.exceptions.ConnectTimeout:
    print("Failed to download the exit addresses list due to a timeout error, please use a VPN.")

try:
    with open('Tor.txt') as f:
        print("Extracting IP Addresses...")
        for line in f:
            match = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            if match:
                torexit = open('Tor-IP-Addresses.txt', 'a')
                torexit.write(match.group() + '\n')
                torexit.close()
    print("Done!")
    os.remove("Tor.txt")
except FileNotFoundError:
    print("")
    
