import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("¿que longitud quieres que tenga tu contraseña (en numero))?"))

pasword =""

for i in range (longitud):
    
    pasword += random.choice(caracteres)

print(pasword)