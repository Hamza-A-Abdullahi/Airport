class Aircraft():
    def __init__(self, type,passenger_capacity, aircraft_model, engin_size):
        self.passenger_cap = passenger_capacity
        self.aircraft_brand = aircraft_model
        self.engin_size = engin_size


class Airplane(Aircraft):
    def __init__(self, passenger_capacity, aircraft_model, engin_size, staff_onboard):
        super().__init__(passenger_capacity, aircraft_model, engin_size)
        self.staff_onboard = staff_onboard
        self.airplane_list= []

    def add_passenger_list(self, aircraft_model, passenger_capacity):
        self.airplane_list.append(aircraft_model)
        self.airplane_list.append(passenger_capacity)


class Helicopter(Aircraft):
    def __init__(self,passenger_capacity, aircraft_model, engin_size):
        super().__init__(passenger_capacity, aircraft_model, engin_size)



