# jm2527 11/26/2023
class DictToObject:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])