import socket
import os


class Scanner:
    def __init__(self):
        self.portsToScan = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 119, 123, 143, 161, 194, 443, 514]
        self.portNames = ['FTP Data Transfer', 'FTP Command Control', 'SSH', 'TELNET', 'SMTP', 'DNS', 'DHCP', 'DHCP',
                          'HTTP', 'POP3', 'NNTP', 'NTP', 'IMAP', 'SNMP', 'IRC', 'HTTPS', 'Remote Shell']

    def GetTarget(self, address):
        if address is str:
            host = socket.gethostbyname(address)
        else:
            host = address
        self.portScan(host, self.portsToScan)

    def portScan(self, target, port):
        for item in port:
            try:
                sock = socket.socket()
                sock.settimeout(0.1)
                sock.connect((target, item))
                print(f'[+] Port {item} Is Open: {self.portNames[port.index(item)]}')
            except:
                pass
        print('..........Port Scanning Is Done!..........\n')
        os.system("pause")


Scanner().GetTarget(address=input('[-] Type In Or Paste Target:'))
