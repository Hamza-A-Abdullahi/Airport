
class Flight():
    def __init__(self,plane,destination,origin):
        self.plane= plane
        self.__destination = destination
        self.__origin = origin
        self.info_passenger = []  # Just an empty list

    def get_destination(self):
        return self.__destination              # destination is private

    def get_origin(self):
        return self.__origin                    # destination is origin


    def get_passengers(self):
        return self.info_passenger

    def flight_details(self):
        passenger_list = []
        for passenger in self.info_passenger:
            passenger_list.append(passenger.get_passenger_detail())
        return f'{self.plane} is going to {self.get_destination().Country} from {self.get_origin().Country},' \
            f' passengers are: {passenger_list}'

    def pass_detail(self):

    def get_passports(self):
        passengers_list = []
        for passenger in self.passengers_list:
            passengers_list.append(passenger.passport_num)
        return passengers_list

