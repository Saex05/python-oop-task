from Complex_Number.ComplexNumberHelper import add_two_numbers, multiply_two_numbers
from Complex_Number.ComplexNumber import ComplexNumber

first_number = ComplexNumber(2, 6)
second_number = ComplexNumber(2, 6)

result_add = add_two_numbers(first_number, second_number)
result_add.print_complex_number()
result_multiply = multiply_two_numbers(first_number, second_number)
result_multiply.print_complex_number()
