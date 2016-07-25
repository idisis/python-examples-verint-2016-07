from sys import argv

hostnames = set(argv[1:])
hosts = {}

# parse hosts file:
with open('hosts', 'r') as hostsFile:
    for line in hostsFile:
        (host, address) = line.split('=', 2)
        if address[-1] == '\n':
            address = address[:-1]
        hosts[host] = address

for name in hostnames:
    if  hosts.has_key(name):
        print hosts[name]
    else:
        print 'hostname \'%s\' not found.' %name

    