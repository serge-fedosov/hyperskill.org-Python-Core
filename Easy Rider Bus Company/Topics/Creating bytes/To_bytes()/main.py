n = int(input())
number_bytes = n.to_bytes(2, byteorder='little')
print(number_bytes[0] + number_bytes[1])
