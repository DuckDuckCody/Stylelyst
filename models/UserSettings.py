class UserSettings:
    def __init__(self):
        self.websites = [2,3,4]
        self.gender = 1
        self.category = 1

    def save_settings(self, settings):
        self.websites = settings.get('websites')
        self.gender = settings.get('gender')
        self.category = settings.get('category')

    def __str__(self):
        return "websites: %s, gender: %s, category: %s" % (self.websites, self.gender, self.category)