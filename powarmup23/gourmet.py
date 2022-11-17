M = int(input()) # minutes
N = int(input()) # dishes
T = [int(input()) for n in range(N)] # time per dish

known_solutions = {}

def solve(m):

    if m not in known_solutions:

        #base cases
        if m == 0:
            # one way to eat, ie eat the currently tested dish
            return 1
        if m < 0:
            # currently tested dish takes to long to eat given remaining time
            return 0

        out = 0
        # test all dishes
        for dish_index in range(N):
            # how many combinations if finishing with dish dish_index'
            out += solve(m-T[dish_index])

        known_solutions[m] = out

    return known_solutions[m]


print(solve(M))
