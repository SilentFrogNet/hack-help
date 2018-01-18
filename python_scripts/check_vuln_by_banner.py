import socket
import argparse
import os
import ipaddress
import re

from termcolor import colored

def getBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return None

def checkVulns(banner, filename):
    f = open(filename, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("    {stat} Server is vulnerable: {bann}".format(
                stat=colored('[+]', 'green'), bann=banner.strip('\n')))

def parseIPs(ips):
    try: 
        if "/" in ips:
            # in CDR format
            nips = re.sub(r".\d+\/", '.0/', ips)
            ip_set = ipaddress.ip_network(nips)
            res = list(ip_set.hosts()) 
            res = [str(x) for x in res]
            return res
        elif "-" in ips:
            # range format
            val = ips.split('-')
            if len(val)>2:
                return None
            res = []
            to_ip_block = int(val[1])
            from_ip = ipaddress.ip_address(val[0])
            from_ip_blocks = val[0].split('.')
            to_num = int(to_ip_block) - int(from_ip_blocks[-1])
            to_ip = from_ip + to_num
            while from_ip <= to_ip:
                res.append(str(from_ip))
                from_ip += 1
            return res
        else:
            # single IP
            return [str(ipaddress.ip_address(ips))]
    except ValueError as e:
        return None


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', action="store", dest="f")
    parser.add_argument('ip')

    results = parser.parse_args()

    vuln_banners_filename = "vuln_banners.txt"
    if results.f and os.path.exists(results.f):
        vuln_banners_filename = results.f

    ips = parseIPs(results.ip)
    
    portList = [21, 22, 25, 80, 110, 443, 8080, 137, 138, 139]
    for ip in ips:
        print('Scanning {ip}...'.format(ip=ip))
        for port in portList:
            banner = getBanner(ip, port)
            if banner:
                print('  {stat} {ip}: {banner}'.format(stat=colored('[+]', 'green'), ip=ip,banner=banner))
                checkVulns(banner, vuln_banners_filename)
            else:
                print('  {stat} {ip}:{port} closed'.format(stat=colored('[-]', 'red'), ip=ip, port=port))


if __name__ == '__main__':
    main()
