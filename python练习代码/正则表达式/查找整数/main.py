import re

s="hello 1234 main 78 rene 900"

ret=re.findall(r'\d+',s)

print(ret)
