def complementary_strand(string):
    result = ""
    for s in string:
        if s == "A":
            result += "T"
        elif s == "T":
            result += "A"
        elif s == "C":
            result += "G"
        elif s == "G":
            result += "C"

    return result


print(complementary_strand(input()))
