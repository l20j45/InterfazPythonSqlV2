import string
import random

length_of_string = int(input("De cuantos caracteres seran los numeros aleatorios?"))
numeroDeAleatorios=int(input("Cuantos aleatorios necesitas?"))
file1 = open('Aleatorios.txt','w')
for x in range(numeroDeAleatorios):
    status1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
    print(status1)
    file1.write(str(status1))
    file1.write("\n")
