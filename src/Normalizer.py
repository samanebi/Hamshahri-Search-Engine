import hazm
class normalizer:
    def __init__(self , data):
        self.data = data


    def normalize(self):
        print("213")
        normalizer = hazm.Normalizer()
        for dict in self.data:
            dict['text'] = normalizer.normalize(dict.get("text"))
            print( normalizer.normalize(dict.get("text")))