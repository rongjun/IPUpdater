#!/usr/bin/python3
# Copyright 2013 Rongjun Tang
import sys
import re
import subprocess
import datetime
from datetime import datetime, date, time
import time
import requests

### Configurations ###
# Afraid.org Web Get Update
# Full URL example: http://freedns.afraid.org/dynamic/update.php?<key>
# Domain key
domain_update_key = "[your-key-here]"
# Afraid.org DNS update URL
domain_update_url = "http://freedns.afraid.org/dynamic/"
domain_update_php = "update.php"
# DynDNS CheckIP URL
check_ip_host = "http://checkip.dyndns.org"
# Sleep time in minutes
sleep_time = 15

### Program ###
def main():
  # Domain Update URL
  update_dns_url = domain_update_url + domain_update_php + "?" + domain_update_key
  # Place hold for current IP Address
  old_ip = ''
  while True:
    try:
      #print('Checking current IP...')
      get_ip = requests.get(check_ip_host)
      #print(get_ip.text)
      my_ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", get_ip.text)
      #print('Current IP Address is:', str(my_ip[0]))

      if str(my_ip[0]) != old_ip:
        #print('IP changed to...', str(my_ip[0]), ': Processing update.')
        update_dns = requests.get(update_dns_url)
        print(update_dns.text)
        print('IP Updated @', str(datetime.now()), ':', str(my_ip[0]))
    except:
      # Catch exception for whatever reason
      print('IPUpdater ERROR!')
    
    # Update place hold IP Address and Sleep
    #print 'Sleeping for', sleep_time, 'mins'
    old_ip = str(my_ip[0])
    time.sleep(sleep_time*60)

if __name__ == '__main__':
  main()
