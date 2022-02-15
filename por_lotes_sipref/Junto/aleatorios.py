import string
import random

number_of_strings = int(input("ingresa el numero de numeros aleatorios: "))
length_of_string = 16
file1 = open('AleatoriosContratos.txt','w')
file2 = open('AleatoriosAbonos.txt','w')
for x in range(number_of_strings):
    status1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    status2 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    print(status1)
    print(status2)
    file1.write(str(status1))
    file1.write("\n")
    file2.write(str(status2))
    file2.write("\n")
