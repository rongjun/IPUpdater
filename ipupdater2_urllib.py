#!/usr/bin/python
# Copyright 2013 Rongjun Tang
import sys
import re
import subprocess
import datetime
from datetime import datetime, date, time
import time
import urllib

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
  #Place hold for IP Address
  old_ip = ''
  while True:
    try:
      #print 'Checking current IP...'
      get_ip = urllib.urlopen(check_ip_host).read()
      my_ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", get_ip)
      #print 'Current IP Address is:', str(my_ip[0])

      if str(my_ip[0]) != old_ip:
        #print 'IP changed to...', str(my_ip[0]), ': Processing update.'
        update_dns_url = domain_update_url + domain_update_php + "?" + domain_update_key
        update_dns = urllib.urlopen(update_dns_url).read()
        print update_dns
        print 'IP Updated @', str(datetime.now()), ':', str(my_ip[0])
    except:
      # Catch exception for whatever reason
      print 'IPUpdater ERROR!'
    
    # Update place hold IP Address and Sleep
    #print 'Sleeping for', sleep_time, 'mins'
    old_ip = str(my_ip[0])
    time.sleep(sleep_time*60)

if __name__ == '__main__':
  main()
