# find_by_obj_attr
# _list: list[obj], key: any, value: any.
# finds the first object in a dictonary list by a specified key's value
def find_by_obj_attr(_list, key, value):
    try:
        item = [d for d in _list if getattr(d, key) == value]
        if item == []:
            return None
        return item[0]
    except AttributeError:
        return None