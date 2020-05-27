"""
Read through a server (e.g., Apache or nginx) logfile. What were the different IP addresses that tried to access your server?
"""

import re
ipAddressRegex = re.compile(r'(^\d+[.]\d+[.]\d+[.]\d+)')

uniqueIPAddresses = set()

with open ('access.log') as f:
  for line in f.readlines():
    if (ipAddressRegex.search(line)):
      ip = ipAddressRegex.search(line).group()
      uniqueIPAddresses.add(ip)


for ipAddress in uniqueIPAddresses:
  print(f"IP: {ipAddress}")