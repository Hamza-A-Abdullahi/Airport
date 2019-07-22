class Passenger():
    def __init__(self,full_name,date_of_birth,gender,nationality,passport_number):
            self.fullname=  full_name   ## change to firstname and surename
            self.date_of_birth = date_of_birth
            self.gender = gender
            self.nationality = nationality
            self.passport_number= passport_number

    # def get_passenger_detail(self):
    #     return  self.full_name,self.gender,self.date_of_birth,
    #     self.nationality,self.passport_number


class Staff():

    def __init__(self,full_name,staff_id):
            self.full_name = full_name
            self.staff_id= staff_id
            self.info_passenger = [] # Just an empty list
            self.flight_info = []

    def book_passenger(self,full_name,date_of_birth,gender,nationality,passport_number):
        self.info_passenger.append(full_name)
        self.info_passenger.append(date_of_birth)
        self.info_passenger.append(gender)
        self.info_passenger.append(nationality)
        self.info_passenger.append(passport_number)



    # def existing_flight (self,list_flight):
    #     return



hamza= Passenger ("Hamza Ali","12/10/1995","Male","British","BR11244")

staff1= Staff("eila","u222")

staff1.book_passenger("Hamza Ali","12/10/1994","Male","British","BR11244")

print(staff1.info_passenger)
