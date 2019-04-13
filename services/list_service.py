# find_by_obj_attr
# lst: list[obj], key: any, value: any.
# finds the first object in a dictonary list by a specified key's value
def find_by_obj_attr(lst, key, value):
    try:
        item = [d for d in lst if getattr(d, key) == value]
        if item == []:
            return None
        return item[0]
    except AttributeError:
        return None