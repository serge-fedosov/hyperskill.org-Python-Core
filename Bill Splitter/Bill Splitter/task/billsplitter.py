friends = {}


def add_friends():
    global friends

    print("Enter the number of friends joining (including you):")
    n = int(input())
    if n <= 0:
        print("No one is joining for the party")
        return 0

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(n):
        name = input()
        friends[name] = 0


if add_friends() != 0:
    print()
    print(friends)
