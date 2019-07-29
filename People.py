
class Passenger():
    def __init__(self, first_name, surename,date_of_birth, gender, nationality, passport_number):
            self.first_name=  first_name
            self.surename= surename
            self.date_of_birth = date_of_birth
            self.gender = gender
            self.nationality = nationality
            self.passport_number= passport_number

    def get_passenger_detail(self):
        return self.first_name + "," + self.surename + "," + self.date_of_birth + "," + self.gender + "," + \
               self.nationality , self.passport_number



class Staff():

    def __init__(self, first_name,surename, staff_id):
            self.first_name = first_name
            self.surname = surename
            self.staff_id= staff_id


    def booking_passenger(self, passenger):
        self.info_passenger.append(passenger)

    def get_passengers(self):
        return self.info_passenger





