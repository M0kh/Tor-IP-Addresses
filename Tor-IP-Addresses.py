import requests
import re
import os

url = 'https://check.torproject.org/exit-addresses'
req = requests.get(url, allow_redirects=True)
open('Tor.txt', 'wb').write(req.content)

with open('Tor.txt') as f:
    for line in f:
        match = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if match:
            torexit = open('Tor-IP-Addresses.txt', 'a')
            torexit.write(match.group() + '\n')
            torexit.close()

os.remove("Tor.txt")
