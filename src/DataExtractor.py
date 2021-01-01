import datetime

class Extractor:
    def __init__(self):
        print()
        self.dataPlace = "../data/Hamshahri-Sample.txt"

    def extract(self):
        with open(self.dataPlace , encoding='utf8') as data:
            temp = ""
            meta = ""
            strings = []
            for line in data:
                if line == "\n":
                    strings.append( {"text" : temp,
                                     "meta" : meta

                                     })
                    temp = ""
                    meta = ""
                else:

                    if line[0:2] != ".D" and line[0:2] != ".C" and line[0:5] != "﻿.DID":
                        temp = temp + line
                    else:
                        meta = meta + line

        return strings





    def compact(self ):
        data = self.extract()
        counter = 0
        result = []
        while counter < len(data):
            temp = {
                "id" : counter ,
                "text" : data[counter].get("text"),
                "meta" : data[counter].get("meta")
            }
            result.append(temp)
            counter = counter + 1
