"""
In URLs, we often replace special and non-printable characters with a % followed by the hexadecimal value of the character’s ASCII value. For example, if a URL is to include a space character (ASCII 32, aka 0x20), we replace it with %20 . Given a string, URL-encode any character that isn’t a letter or number. For the purposes of this exercise, we’ll assume that all characters are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It might help to know about the ord ( docs.python.org/3/library/functions.html?#ord ) and hex ( docs.python.org/3/library/functions.html?#hex ) functions.
"""

def encodeURL(urlString):
    result = []
    for letter in urlString:
        if (ord(letter) >= 48 and ord(letter) <= 57) or (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122):
            result.append(letter)
        else:
            result.append('%' + format(ord(letter),'02x'))
    return ''.join(result)



print (encodeURL('docs.python.org/3/library/functions.html?#ord'))
print (encodeURL('docs.python.org/3/library/functions.html?#hex'))
