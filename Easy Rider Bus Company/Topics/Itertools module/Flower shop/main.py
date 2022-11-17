import itertools

for i in range(1, 4):
    flowers = itertools.combinations(flower_names, i)
    for flower in flowers:
        print(flower)
