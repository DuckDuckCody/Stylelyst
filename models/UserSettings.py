class UserSettings:
    def __init__(self, settings):
        if bool(settings): 
            self.load_settings(settings)
        else:
            self.website_ids = [1]
            self.gender_id = 1
            self.category_id = 1

    def load_settings(self, settings):
        self.website_ids = list(map(int, settings.get('website_ids').split(',')))
        self.gender_id = int(settings.get('gender_id'))
        self.category_id = int(settings.get('category_id'))

    def __str__(self):
        return "website_ids: %s, gender_id: %s, category_id: %s" % (self.website_ids, self.gender_id, self.category_id)