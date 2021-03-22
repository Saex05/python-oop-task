import time

from Ex_5_Parking_Ticket.Parking import Parking

if __name__ == '__main__':
    parking = Parking()
    parking.car_output("VOLVO")
    parking.car_input("FORD")
    parking.car_input("NISSAN")
    parking.car_input("MAZDA")
    parking.car_input("AUDI")
    parking.car_input("FERRARI")
    parking.car_input("LANDA")
    time.sleep(2)
    parking.car_output("LANDA")
    time.sleep(2)
    parking.car_output("FORD")
    time.sleep(2)
    parking.car_output("NISSAN")
    pass
