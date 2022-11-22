m,_,c=open(o:=0)
c=sorted(map(int,c.split()))
for s in c:o+=s*c[~o]>=int(m)
print(o//2)
