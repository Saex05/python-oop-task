from datetime import datetime
from Ticket import Ticket


class Parking:
    def __init__(self, name="Parking Z"):
        self.name = name
        self.maximum_number_of_cars = 5
        self.ticket_list = []

    def car_input(self, car_name):
        if len(self.ticket_list) <= self.maximum_number_of_cars-1:
            ticket = Ticket(car_name, datetime.now())
            self.ticket_list.append(ticket)

        else:
            print("{} is full, the car({}) did not enter.".format(self.name, car_name))

    def car_output(self, car_name):
        if not self.ticket_list:
            print("{} is empty, the car({}) does not exit".format(self.name, car_name))

        for ticket in self.ticket_list:
            if ticket.name == car_name:
                ticket.create_ticket()
                self.ticket_list.remove(ticket)
                break
        else:
            print("The car with name({}) does not exit in the car park".format(car_name))
