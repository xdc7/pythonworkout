"""
Write a program to read /etc/passwd on a Unix computer. The first field contains the username, and the final field contains the user’s "shell," the command interpreter. Display the shells in decreasing order of popularity, such that the most-popular shell is shown first, the second-most popular shell second, and so forth. For an added challenge, after displaying each shell, also show the usernames (sorted alphabetically) who use each of those shells.
""" 
import operator
from collections import Counter

passwdFile = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
userx:x:1000:1000:,,,:/home/userx:/bin/bash"""

# passwdFile = """
# root:x:0:0:root:/root:/bin/bash
# root2:x:0:0:root:/root:/bin/bash
# """

def sortDict(shellDict):
    print (shellDict)

def most_popular_shell(passwdFile):
    shells = {}
    for line in passwdFile.split('\n'):
        if not line:
            continue
        shell = line.split(':')[-1]
        user = line.split(':')[0]
        if shells.get(shell):
            shells[shell]['count'] += 1
            shells[shell]['users'].append(user)
        else:
            shells[shell] = {'count' : 1, 'users' : [user]}
   
    # Easier way to understand how the sorting works
    # items =  sorted(tuple(shells.items()), key=lambda item: item[1].get('count'), reverse=True)
    # result = {}
    # for item in items:
    #     result[item[0]] = sorted(item[1].get("users"))
    
    # One-liner or a more 'pythonic way'
    result = {item[0]: f' {sorted(item[1].get("users"))}' for item in sorted(tuple(shells.items()), key=lambda item: item[1].get('count'), reverse=True)}

    return result
    
print (most_popular_shell(passwdFile))


