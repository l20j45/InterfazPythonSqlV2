import string
import random

number_of_strings = int(input("ingresa el numero de numeros aleatorios"))
length_of_string = 16
file = open('Aleatorios.txt','w')
for x in range(number_of_strings):
    status = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    print(status)
    file.write(str(status))
    file.write("\n")