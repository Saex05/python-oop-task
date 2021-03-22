"""
I would like to change my first option that was 20 for 2000
"""
options = [5, 10, 15, 20, 25, 30, 4, 20]
for index, option in enumerate(options):
    if option == 20:
        options[index] = 2000

print(options)
