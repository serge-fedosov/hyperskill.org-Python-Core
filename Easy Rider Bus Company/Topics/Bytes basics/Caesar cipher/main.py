string = input()
new_string = ""
for s in string:
    new_string += chr(ord(s) + 1)

print(new_string)
