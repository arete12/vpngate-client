import requests
import io
import csv
import base64
import random
import os

print("Connecting to VPNGate...")
req = requests.get("http://www.vpngate.net/api/iphone")
data = io.BytesIO(req.text.encode("utf-8"))

next(data)
reader = csv.DictReader(data)
vpns = []

print("Choosing VPN...")
for x in reader:
    vpns.append(x["OpenVPN_ConfigData_Base64"])

del vpns[-1]
randvpn = random.randint(0, len(vpns))
vpn = vpns[randvpn]

path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(path, "vpn.ovpn")

f = open("vpn.ovpn", "w")
f.write(base64.b64decode(vpn))
f.close()
print("Connecting to VPN...")
