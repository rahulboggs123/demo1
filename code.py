import re

fhand=open('actual.txt')
numlist=list()
for line in  fhand:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    for r in stuff:
        numlist.append(int(r))
print(sum(numlist))