from collections.abc import Hashable


objects_dict = {}
for obj in objects:
    if isinstance(obj, Hashable):
        objects_dict[obj] = hash(obj)
