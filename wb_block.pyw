import time
from datetime import datetime as dt

temp_hosts = 'hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
web_block_list = ['www.facebook.com','facebook.com','ebay.co.uk','www.ebay.co.uk','www.wp.pl','wp.pl']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('Working hours....')
        with open(hosts_path, 'r+') as file:
            contetnt = file.read()
            for websites in web_block_list:
                if websites in contetnt:
                    pass
                else:
                    file.write(redirect+' '+websites+'\n')

    else:
        with open(hosts_path, 'r+') as file:
            contetnt = file.readlines()
            file.seek(0)
            for lines in contetnt:
                if not any(websites in lines for websites in web_block_list):
                    file.write(lines)
            file.truncate()
        print('You are off....')
    time.sleep(5)
