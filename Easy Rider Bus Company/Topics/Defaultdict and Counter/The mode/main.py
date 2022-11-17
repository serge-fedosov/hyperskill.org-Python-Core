from collections import Counter

text_list = input().split(" ")

freq_counter = Counter(text_list)
val = freq_counter.most_common(1)
print(val[0][0])
