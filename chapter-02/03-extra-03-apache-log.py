"""
Read through an Apache logfile. If there is a 404 error — you can just search for ' 404 ', if you want — then display the IP address, which should be the first element.

"""
import re
found404Regex = re.compile(r'(\s404\s)')
ipAddressRegex = re.compile(r'(\d+[.]\d+[.]\d+[.]\d+)')
counter = 0
with open ('access.log') as f:
    for line in f.readlines():
        # An alternate way to find the ' 404 ' string without using regex:
        # if  ' 404 ' in line:
        if found404Regex.search(line):
            counter += 1
            ipAddress = ipAddressRegex.search(line).group()
            print (ipAddress)
            # An alternate way to print the IP address without using regex:
            # print (line.split()[0])
print (f'number of 404s: {counter}')