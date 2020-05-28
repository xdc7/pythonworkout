"""
Read through a server (e.g., Apache or nginx) logfile. What were the different IP addresses that tried to access your server?
Reading from that same server log, what were the different response codes that were
returned to users? 200 represents "OK," but there are also 403, 404, and 500 errors.
(Regular expressions aren’t required here, but will probably help.)
"""

# "GET /administrator/ HTTP/1.1" 200 4

import re
httpStatusCodeRegex = re.compile(r'((HTTP[/]\d.*["]\s)(\d\d\d)\s)')
ipAddressRegex = re.compile(r'(^\d+[.]\d+[.]\d+[.]\d+)')

uniqueIPAddresses = set()

with open ('access.log') as f:
  for line in f.readlines():
    if (httpStatusCodeRegex.search(line)):
      statusCode = httpStatusCodeRegex.search(line).group(3)
      ip = ipAddressRegex.search(line).group()
      uniqueIPAddresses.add("IP: {0:16} HTTP status code: {1:30}".format(ip, statusCode))


for ipAddress in uniqueIPAddresses:
  print(ipAddress)