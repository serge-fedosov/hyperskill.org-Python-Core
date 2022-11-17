import copy

def my_copy(obj, copy_mode):
    return obj.copy() if copy_mode == "shallow copy" else copy.deepcopy(obj)
