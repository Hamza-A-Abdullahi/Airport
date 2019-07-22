from People import Staff

class Flight():
    def __init__(self,plane,destination,orgin,passenger_list=[]):
        self.plane= plane
        self.passenger_list=passenger_list
        self.destination= destination
        self.orgin= orgin

    def cancel_flight(self):
        return "Your Flight has been cancelled"


