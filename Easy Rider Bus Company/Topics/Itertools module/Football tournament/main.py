import itertools

# the variable 'teams' is already defined
my_iter = itertools.combinations(teams, 2)

for i in my_iter:
    print(i)
