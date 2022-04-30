# Tarea 1
inversion = int(input('Ingrese la cantidad a invertir: '))
interes_anual = float(input('Ingrese interes anual: '))
anios = int(input('Ingrese cantidad de años: '))

capital = inversion * (1 + interes_anual) ** anios

print(capital)

#Tarea 2
n = int(input('Ingrese el primer numero: '))
m = int(input('Ingrese el segundo numero: '))
c = n // m
r = n % m

print('Cociente:', str(c))
print('Resto', str(r))

#Tarea 3
peso = float(input('Ingrese su peso en Kg.: '))
altura = float(input('Ingrese su altura en metros: '))

imc = peso / (altura)**2

print('Su IMC es:', round(imc, 2))