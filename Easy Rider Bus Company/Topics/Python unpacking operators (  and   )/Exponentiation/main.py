info = input().split(', ')
# your code here
name, age, city, *miscellaneous = info
print(f"""name: {name}
age: {age}
city: {city}
miscellaneous:""", *miscellaneous)
