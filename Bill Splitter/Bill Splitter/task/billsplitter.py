import random

friends = {}


def add_friends():
    global friends

    print("Enter the number of friends joining (including you):")
    n = int(input())
    if n <= 0:
        return 0

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(n):
        name = input()
        friends[name] = 0

    return n


def update_bill(n, lucky=False):
    global friends

    for friend in friends:
        if lucky and friend == lucky:
            friends[friend] = 0
        else:
            friends[friend] = n


def main():
    global friends

    n = add_friends()
    if n == 0:
        print("No one is joining for the party")
        return

    print("Enter the total bill value:")
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()

    bill_for_each = 0
    if answer == "Yes" and n != 1:
        bill_for_each = round(bill / (n - 1), 2)
        lucky = list(friends.keys())[random.randint(0, n - 1)]
        print(f"{lucky} is the lucky one!")
        update_bill(bill_for_each, lucky)
    else:
        bill_for_each = round(bill / n, 2)
        print("No one is going to be lucky")
        update_bill(bill_for_each)

    # print()
    # print(friends)


main()
