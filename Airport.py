class Airport:
    def __init__(self, AirportName, Country, IsInternational=True):      #default set value, can set it to false when creating an object of the class
        self.AirportName = AirportName
        self.Country = Country
        self.IsInternational = IsInternational