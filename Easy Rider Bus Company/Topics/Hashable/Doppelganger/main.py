from collections.abc import Hashable

# the object_list has already been defined
hash_dict = {}
for obj in object_list:
    if isinstance(obj, Hashable):
        hash_dict[hash(obj)] = 0

for obj in object_list:
    if isinstance(obj, Hashable):
        hash_dict[hash(obj)] += 1

count = 0
for hash_el in hash_dict:
    if hash_dict[hash_el] != 1:
        count += hash_dict[hash_el]

print(count)
