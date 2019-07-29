from Aircraft import Airplane
from People import Passenger
from Flight import Flight
from Airport import Airport


plane1 = Airplane('737','Boeing')
plane2 = Airplane('A350','Airbus')


airport1 = Airport('Heathrow', 'England', True)    # create an object of Airport
airport2 = Airport('LAX', 'USA', True)
airport3=  Airport('Hamza Int','Italy',True)

flight1 = Flight(plane1, airport1, airport2)       # use the object you have used
flight2= Flight(plane1,airport1,airport3)

passenger1 = Passenger('Hamza', 'Bull',"12/12/1992","male","British",11122564)


print(passenger1.get_passenger_detail(),)


