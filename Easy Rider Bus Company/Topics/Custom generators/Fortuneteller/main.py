n = int(input())
sum_ = 0
while n != 0:
    sum_ += n % 10
    n //= 10

print(sum_)
