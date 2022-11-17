three_months = input().split()

three_months_tuple = (three_months[0], three_months[1], three_months[2])
if three_months_tuple in months:
    print("True")
else:
    print("False")
