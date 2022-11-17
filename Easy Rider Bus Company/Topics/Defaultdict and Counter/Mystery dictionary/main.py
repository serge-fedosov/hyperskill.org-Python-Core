# `random_dict` has been defined
# the input is in the variable `word`
# write the rest of the code here

random_dict.setdefault(word, [])
if random_dict[word] == []:
    print("Not in the dictionary")
else:
    print(random_dict[word])
