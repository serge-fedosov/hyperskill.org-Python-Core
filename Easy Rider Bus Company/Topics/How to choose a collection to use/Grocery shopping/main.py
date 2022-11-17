from collections import Counter

shopping_list = input().split()
freq_counter = Counter(shopping_list)
for key in freq_counter:
    print(freq_counter[key], key)
