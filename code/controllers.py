class Controllers():
    def __init__(self):
        self.preferences = None

    def save_preferences(self, preferences_dict):
        self.preferences = preferences_dict
        print self.preferences