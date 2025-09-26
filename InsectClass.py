import random

class Insect:
    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.flight = 0


    def flight_length(self):
        self.flight = random.randint(1,10)
        return self.flight
    
    def get_miles(self):
        return self.flight
    
