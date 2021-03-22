from datetime import datetime


class Ticket:
    def __init__(self, name, input_time):
        self.name = name
        self.input_time = input_time
        self.ticket = {}

    def create_ticket(self):

        actual_time = datetime.now()

        self.ticket.setdefault("car_name", self.name)
        self.ticket.setdefault("date", actual_time.date())
        self.ticket.setdefault("input", self.input_time.time())
        self.ticket.setdefault("output", actual_time.time())

        rest_of_time = actual_time - self.input_time
        paid = rest_of_time.seconds * 10
        self.ticket.setdefault("paid", paid)
        self.__print_ticket()

    def __print_ticket(self):
        print("*****************************")
        print("Car name: {}".format(self.ticket['car_name']))
        print("Check For Parking")
        print("      {}      ".format(self.ticket['date']))
        print("FROM: {} {}".format(self.ticket['date'], self.ticket['input']))
        print("TO: {} {}".format(self.ticket['date'], self.ticket['output']))
        print("Paid: {}".format(self.ticket['paid']))
        print("*****************************")

