class UserSettings:
    def __init__(self, settings):
        if bool(settings): 
            self.load_settings(settings)
        else:
            self.websites = [1]
            self.gender = 1
            self.category = 1

    def load_settings(self, settings):
        self.websites = list(map(int, settings.get('websites').split(',')))
        self.gender = int(settings.get('gender'))
        self.category = int(settings.get('category'))

    def __str__(self):
        return "websites: %s, gender: %s, category: %s" % (self.websites, self.gender, self.category)