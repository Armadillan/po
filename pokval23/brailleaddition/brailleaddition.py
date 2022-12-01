translation = {
    "*.....": "1",
    "*.*...": "2",
    "**....": "3",
    "**.*..": "4",
    "*..*..": "5",
    "***...": "6",
    "****..": "7",
    "*.**..": "8",
    ".**...": "9",
    ".***..": "0",
}

inv_translation = {v: k for k, v in translation.items()}

input()
number0 =  zip(*[input().split() for _ in range(3)])
number0 = ["".join(x) for x in number0]
number0 = int("".join(translation[x] for x in number0))

input()
number1 =  zip(*[input().split() for _ in range(3)])
number1 = ["".join(x) for x in number1]
number1 = int("".join(translation[x] for x in number1))

out = list(str(number0 + number1))
out = [inv_translation[x] for x in out]
out = [[x[i:i+2] for i in range(0, len(x), 2)] for x in out]
out = zip(*out)
out = [" ".join(x) for x in out]
for x in out:
    print(x)
