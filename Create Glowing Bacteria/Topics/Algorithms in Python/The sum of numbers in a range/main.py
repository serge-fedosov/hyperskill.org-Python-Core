def range_sum(numbers, start, end):
    sum_in_range = 0
    for n in numbers:
        if start <= n <= end:
            sum_in_range += n

    return sum_in_range


input_numbers = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
print(range_sum(input_numbers, a, b))
