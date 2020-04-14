# vpngate-client

A client to download a random VPN from [VpnGate](http://vpngate.net) and then connecting to it.

__Features__:
* deletes all .ovpn files in the current directory
* goes to http://vpngate.net and chooses a random VPN, downloading it
* connects to the VPN

## Dependencies
* [Python](https://python.org) v2
* [OpenVPN](https://openvpn.net/)
* requests module that Python can't import (pip install requests)

## Usage
```shell
  sudo chmod +x ./vpn.sh
  sudo ./vpn.sh
```
