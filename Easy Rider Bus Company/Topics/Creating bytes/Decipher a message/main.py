string = input()
n = int(input())
encoded_string = string.encode()
int_to_bytes = n.to_bytes(2, 'little')
sum_ = int_to_bytes[0] + int_to_bytes[1]

characters = bytes([x + sum_ for x in encoded_string])
print(characters.decode())

