m,_,c=open(0)
c=sorted(map(int,c.split()))
o=-1
print(len([o:=o-1for s in c if s*c[o]>=int(m)])//2)
