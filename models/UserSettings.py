class UserSettings:
    def __init__(self):
        self.websites = [2]
        self.gender = 1
        self.category = 1
        self._current_page = 0

    def save_settings(self, settings):
        self.websites = settings.get('websites')
        self.gender = settings.get('gender')
        self.category = settings.get('category')

    @property
    def current_page(self):
        return str(self._current_page)

    @current_page.setter
    def current_page(self, page):
        if page is None:
            page = 1
        self._current_page = page

    def __str__(self):
        return "websites: %s, gender: %s, category: %s, current_page: %s" % (self.websites, self.gender, self.category, self.current_page)