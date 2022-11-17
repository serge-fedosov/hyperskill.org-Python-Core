def tallest_people(**kwargs):
    max_ = max(kwargs.values())
    for key, value in sorted(kwargs.items()):
        if value == max_:
            print(f"{key} : {value}")

