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


def update_bill(n):
    global friends

    for friend in friends:
        friends[friend] = n


if add_friends() != 0:
    print("Enter the total bill value:")
    bill = int(input())
    bill_for_each = round(bill / len(friends), 2)
    update_bill(bill_for_each)

    print()
    print(friends)
