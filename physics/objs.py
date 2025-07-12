import pandas as pd
import random

class Body:
    def __init__(self, date, typeof):
        self.typeof = typeof
        self.date = date
        self.properties = {
            "density" : 0,
            "electrical-resistivity" : 0,
            "electrical-conductivity" : 0,
            "saturation" : 0,
            "cohesion" : 0,
            "moisture" : 0,
            "WRC" : 0,
            "pore-pressure" : 0,
            "hardness" : 0
        }
        self.RandomgPropertiesAssigner()

    def RangeSetter(self, prop):
        df = pd.read_csv("properties_ranges.csv")
        data = df.loc[self.typeof, prop]
        min_val = ""
        max_val = ""
        for i in data:
            val = val + i
            if i is '-':
                min_val = val
                val = ""
            if i is '\n':
                max_val = val
        return max_val, min_val

    
    def RandomPropertiesAssigner(self):
        for prop in self.properties:
            min_val, max_val = RangeSetter(prop)
            val = random.randint(min_val, max_val)
            self.properties[prop] = val


class Soil(Body):
    def __init__(self):
        self.RandomPropertiesAssigner()


