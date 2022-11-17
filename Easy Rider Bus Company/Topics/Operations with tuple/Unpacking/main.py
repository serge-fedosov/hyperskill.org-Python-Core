def unpack(input_tuple):
    unpacked = ()
    for el in input_tuple:
        if isinstance(el, str):
            unpacked = unpacked + (el,)
        else:
            unpacked = unpacked + el

    return unpacked
