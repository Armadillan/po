m,_,c=open(o:=0)
c=sorted(map(int,c.split()))
for s in c:o-=(0,1)[s*c[o-1]>=int(m)]
print(o//-2)
