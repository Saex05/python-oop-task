import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)


class ComplexNumber:
    def __init__(self, real_number, imaginary_number):
        self.__real_number = real_number
        self.__imaginary_number = imaginary_number
        logging.info("{} {}i".format(self.__real_number, self.__imaginary_number))

    def get_imaginary_number(self):
        return self.__imaginary_number

    def get_real_number(self):
        return self.__real_number

    def print_complex_number(self):
        print("{} {}i".format(self.__real_number, self.__imaginary_number))
