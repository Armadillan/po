from z3 import *

#indata!!!
people = list(map(int, input().split()))

# gör om indatan till en Z3-array
A = Array('A', IntSort(), IntSort())
i = 0
for elem in people:
  A = Store(A, i, elem)
  i = i + 1

# lista 0...n-1 där n är antalet människor
# alltså en lista med alla index i people
indices = [x for x in range(len(people))]

# data relevant för uppgiften
half_strength = sum(people)//2
half_length = len(people)//2

# en representation av utdatan (ena laget) som "lista" (vektor) av heltal
# på grund av hur Z3 funkar så innehåller listan indexen för varje
# lagmedlem, styrkan på människa i är people[i]
# eller Select(A, i) i Z3
vec = IntVector("x", half_length)


# Här börjar vi berätta för Z3 vad problemet är
s = Solver()
# varje element i vec måste vara unikt
# (vi kan inte ha samma människa flera gånger)
s.add(Distinct(vec))
# summan av alla lagmedlemmarnas styrkor måste vara lika med
# halva den totala styrkan
s.add(sum(Select(A, x) for x in vec)==half_strength)
# alla element i vec är index i people, alltså är de:
# större än eller lika med noll, och
s.add(And([0<=x for x in vec]))
# mindre än längden av people
s.add(And([x<len(people) for x in vec]))

# kolla ifall modellen är satisfiable
# vi behöver inte spara det här för vi vet att den är det enligt uppfigten
# men vi behöver köra funktionen för att få ut en modell
s.check()
# vi sparar modellen som Z3 hittar
m = s.model()
# och skapar lista på lagmedlemmarnas styrkor
# genom att extrahera varje variabel
# (element i i vec för varje i<halva totala antalet människor)
# ur vec och ta motosvarande element ur people
# .as_long() krävs här iom Z3-integers inte är samma som python-integers
out = [people[m[vec[i]].as_long()] for i in range(half_length)]
# sortera, gör till sträng, skriv ut
print(" ".join(map(str,sorted(out))))
