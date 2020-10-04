import re
from string import digits
req=''

with open('rawframe.txt', 'r') as f:
    req = f.read()



remove_digits = str.maketrans('', '', digits)
res = req.translate(remove_digits)

print(res)

with open('cleanedframe.txt', 'w') as f:
    f.write(res)


