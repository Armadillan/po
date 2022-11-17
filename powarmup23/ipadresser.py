import re

def insert(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

regex = re.compile(r"^(0|([1-9][0-9]{0,2}))\.(0|([1-9][0-9]{0,2}))\.(0|([1-9][0-9]{0,2}))\.(0|([1-9][0-9]{0,2}))$")

s = input()

l = len(s)

out = 0

for i in range(1, l-2):
    for j in range(i, l):
        for k in range(j, l+2):
            tmp = insert(s, ".", i)
            tmp = insert(tmp, ".", j)
            tmp = insert(tmp, ".", k)

            m = regex.match(tmp)
            if m is not None:
                #ugly but whatevs
                ok = True
                for g in (1,3,5,7):
                    if int(m.group(g)) > 255:
                        ok = False
                if ok:
                    out += 1


print(out)
