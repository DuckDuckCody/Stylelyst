def find_by_obj_attr(lyst, key, value):
    if lyst == [] or lyst == None:
        return None
    else:
        item = [d for d in lyst if getattr(d, key) == value]
        if item == []:
            return None
        return item[0]