from localroku.core import Roku
import re
import binascii

#roku = Roku('192.168.1.189')
roku = Roku('192.168.1.2')

#devices = Roku.discover(timeout=5)
#print(devices)


print(roku.active_app)
netflix = roku['Netflix']
#netflix.launch()
#netflix.store()

#print(roku.commands)

def get_channelurl(ip):
    app_id = re.findall('Application: \[(.*)]', str(roku.active_app))[0]
    return (f'http://{ip}:8060/query/icon/{app_id}')



get_channelurl(ip='192.168.1.2')
#for i in devices:
    #print(i)
#    text = re.findall("Roku: (.*)>", str(i))
#    print(text)


'''
import ipaddress

network = [str(ip) for ip in ipaddress.IPv4Network('192.168.1.0/24')]
print(network)
network = ['192.168.1.2']
for i in network:
    try:
        roku = Roku(i, timeout=0.05)
        print(roku.device_info)
    except:
        pass



import arpreq
print(arpreq.arpreq('192.168.1.2'))

def arpreq_ip(ip):
    data = arpreq.arpreq(ip)
    try:
        if "c8:3a:6b" in data:

            return True
    except:
        return False


#print(arpreq_ip('192.168.1.189'))

import ipaddress

network = [str(ip) for ip in ipaddress.IPv4Network('192.168.1.0/24')]
print(network)

network = ['192.168.1.2']

for ip in network:
    check = arpreq_ip(ip)
    print(check)



import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
sockname = s.getsockname()[0]
s.close()
ipaddr = re.findall('(.*\.)', sockname)

import ipaddress
network = [str(ip) for ip in ipaddress.IPv4Network(ipaddr[0] + '0/24')]
#print(network)

result = []
count = 0
for i in network:
    try:
        roku = Roku(i, timeout=0.1)
        roku.device_info
        count = count + 1
        result += [i]
    except:
        pass

print(count)
print(result)
'''