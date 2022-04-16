# #### Ejercicio
# Una máquina tragamonedas tiene la siguiente fórmula para determinar si alguien gana premio:
# - La apuesta inicial siempre tiene que ser un número mayor a 0
# - La apuesta inicial se divide entre 15
# - Se toma la parte entera de la división y si es mayor a 0, se multiplica por (3 + el residuo); si es igual a 0, se le agrega 1.5 y se multiplica por el residuo del paso anterior 
# 
# Ejemplo del paso anterior
#     - si la apuesta era 2, dividir 2 entre 15 da un cociente entero de 0 y un residuo de 2. Entonces el resultado del paso anterior es 1.5 * 2
#     - si la apuesta era 34, dividir 34 entre 15 da un cociente entero de 2 y un residuo de 4. Entonces el resultado del paso anterior es 2 * (3+4)
# 
# 
# - Finalmente, si el resultado es divisible entre 7, el jugador gana.
# 
# 
# Ejemplo, apuesta inicial: 24.
# Apuesta inicial entre 15: 1, residuo 9.
# 1 * (3 + 9) = 12
# El residuo de dividir 12 / 7 no es igual a 0.
# El jugador no gana.
#
# Supongamos que hay un bug en la máquina de apuestas y ocasionalmente lee las apuestas como números negativos. Modifica tu código para que al leer la apuesta, lo cambie a un número positivo.

apuesta = 24

cociente = apuesta//15
residuo = apuesta%15

print("cociente = " + str(cociente))
print("cociente = " + str(residuo))

if apuesta < 0:
    apuesta = (apuesta**2)**(1/2) # Ya que no hemos visto numpy :P

if cociente > 0:
    res = cociente*(3+residuo)
else: 
    res = (cociente+1.5)*residuo
if res%7 == 0:
    print("¡Si sí por supuesto awuebi, ganaste!")
else:
    print("F, perdiste")