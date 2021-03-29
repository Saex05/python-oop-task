from Complex_Number.ComplexNumber import ComplexNumber


def add_two_numbers(first_number: ComplexNumber, second_number: ComplexNumber):
    real_number = first_number.get_real_number() + second_number.get_real_number()
    imaginary_number = first_number.get_imaginary_number() + second_number.get_imaginary_number()
    return ComplexNumber(real_number, imaginary_number)


def multiply_two_numbers(first_number: ComplexNumber, second_number: ComplexNumber):
    first_term = first_number.get_real_number() * second_number.get_real_number()
    second_term = first_number.get_real_number() * second_number.get_imaginary_number()
    third_term = first_number.get_imaginary_number() * second_number.get_real_number()
    fourth_term = first_number.get_imaginary_number() * second_number.get_imaginary_number() * -1

    real_number = first_term + fourth_term
    imaginary_number = second_term + third_term

    return ComplexNumber(real_number, imaginary_number)



