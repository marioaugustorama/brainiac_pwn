import nmap
nm = nmap.PortScanner()

nm.scan('192.168.23.100/24', arguments='-sP', sudo=True)
for h in nm.all_hosts():
    if 'mac' in nm[h]['addresses']:
        print('mac address found: {}'.format(nm[h]['addresses']))
        print('vendor: {}'.format(nm[h]['vendor']))