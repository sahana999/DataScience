x=input("enter file1")
f=open(x,'r')
st=f.read(500)
c=0
d=0
e=0
f=0
for r in st:
    if r.isdigit():
        c=c+1
    if r.isupper():
        d=d+1
    if r.islower():
        e=e+1
print('Digits',c)
print('upper',d)
print('lower',e)


