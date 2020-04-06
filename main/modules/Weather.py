class Wind:
    def __init__(self):
        self.min = 0
        self.max = 0
        self.avarage = 0
        self.direction = 0

class Temperature:
    def __init__(self):
        self.min = 0
        self.max = 0
        self.avarage = 0

class Pressure:
    def __init__(self):
        self.min = 0
        self.max = 0
        self.avarage = 0
    

class Weather:
    def __init__(self, data, sol):
        self.sol = sol

        self.date = data["First_UTC"][:10]

        self.at = Temperature()

        self.at.min = round(int(data["AT"]["mn"]))
        self.at.max = round(int(data["AT"]["mx"]))
        self.at.avarage = round(int(data["AT"]["av"]))

        self.wind = Wind()

        self.wind.min = round(int(data["HWS"]["mn"]))
        self.wind.max = round(int(data["HWS"]["mx"]))
        self.wind.avarage = round(int(data["HWS"]["av"]))
        self.wind.direction = data["WD"]["0"]["compass_point"]

        self.pre = Pressure()

        self.pre.min = round(int(data["PRE"]["mn"]))
        self.pre.max = round(int(data["PRE"]["mx"]))
        self.pre.avarage = round(int(data["PRE"]["av"]))



        
    