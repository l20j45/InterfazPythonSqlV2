import string
import random

number_of_strings = int(input("ingresa el numero de numeros aleatorios: "))
length_of_string = 14
file1 = open('AleatoriosColonias.txt','w')
for x in range(number_of_strings):
    status1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    print(status1)
    file1.write(str(status1))
    file1.write("\n")
