i=input
m=int(i())
i()
c=sorted(int(x)for x in i().split())
o=-1
print(len([o:=o-1for s in c if s*c[o]>=m])//2)
