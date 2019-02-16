class ObjectManager:
    def __init__(self):
        return None

    def get(self, object, key, value):
        if object == [] or object == None:
            return None
        else:
            item = [d for d in object if d[key] == value]
            if item == []:
                return None
            else:
                return item[0]