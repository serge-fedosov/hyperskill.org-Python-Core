import re

word = input()
if re.match(r'the\b', word):
    print("True")
else:
    print("False")
