class ListManager:
    def __init__(self):
        return None

    def find_by_obj_attr(self, object, key, value):
        if object == [] or object == None:
            return None
        else:
            item = [d for d in object if getattr(d, key) == value]
            if item == []:
                return None
            else:
                return item[0]