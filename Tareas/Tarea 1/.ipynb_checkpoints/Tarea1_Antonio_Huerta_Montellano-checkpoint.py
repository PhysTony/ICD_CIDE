"""
Ejercicio 1:

Explicar por qué un modelo predictivo no es capaz de explicar relaciones causales. 

Antes que nada, aunque parezca una obviedad, un modelo predictivo está enfocado en predecir valores fuera del conjunto con el que se armó, no se enfoca en las relaciones causales o explicativas que provocan el fenómeno a prededir. Uno de los propósitos o caraceterísticas d elos modelos predictivos es minimizar el error entre los valores predichos y los reales fuera del conjunto de entrenamiento, independientemente de si el modelo sea simple, complejo, el verdadero o no. Entonces, puede ocurrir que el modelo sea bueno prediciendo, pero que no tenga sentido interpretativo, o teórico, o que no concuerde con el modelo teórico propuesto, es deicr, puede ser bueno prediciendo valores, pero no te asegura que sea el modelo teórico.

Un ejemplo de esto se puede apreciar en el fenómeno de la catástrofe ultravioleta donde se dieron, en un inicio, dos modelos que explicaban dicho fenómeno para rangos de longitud de ondas distintos. Si bien, en sus respectivos rangos daban muy buenas predicciones, fallaban en dar algún entendimiento del fenómeno a pesar de obtener buenos resultados predictivos. Sin embargo, la ecuación de Max Planck sí pudo dar un entendimiento teórico y además, predictivo.
"""

"""
Ejercico 2: 

¿Que se requiere para que un modelo empírico pueda ser utilizado como guía para la implementación de políticas públicas? 

Primero, dependerá del propósitode la política pública ya que no es lo mismo que el objetivo sea predecir algún factor determinado o más bien, entender cierto fenómeno; esto porque alguna herramienta auxiliar sería algún modelo que complemente o mejore los aspectos explicativos o predictivos del empírico. Sin embargo, nos tendríamos que restringir a dos tipos de modelos: Explicativo y predictivo, por razones asociadas a la ley de Goodhardt y los otros aspectos mencionados en el artículo como el etiquetado y preregistro. Por otro lado, se podrían combinar ambos modelos para ofrecer una mayor entendimiento sin tener que usar algún modelo integrado (donde podríamos obtener un menor entendimiento).

Si solo quisiéramos usar el modelo empírico, habría que tomar en cuenta en qué región o bajo qué condiciones específicas funciona, ya que no necesariamente se obtendrán los mismo resultados en distintas regiones geofráficas. Esto, implica que se tendría que buscar datos, directao indirectamente, que sustenten que a la región donde se aplicaría la política pueda funcionar (esto si no se aplicaría a la misma región con la cual fue construido el modelo empírico). Además, habría que considerar los puntos mencionados en el párrafo anterior. Por otro lado, tomar en cuenta que los factores o efectos que considera el modelo empírico inicial podrían cambiar a lo largo del tiempo, por lo que se tendría que estar evaluando cada determinado intervalo de tiempo.

"""

"""
Ejercicio 3:

Escribe un programa de Python en el que puedas encontrar el máximo valor de una lista o secuencia (utiliza un iterador).

El algorítmo consiste en que se compararán todas las entradas de la lista una por una con respecto a un entrada en particular para ver cuál es la más grande. Crearemos una variable auxiliar que este  inicializada en la primera entrada de la lista, luego compararemos esta variable con las demás entradas
de la lista, si alguna de las otras entradas contiene un valor más grande que nuestra variable auxiliar, se le asignará ese valor a la variable auxiliar. Para esto, será necesario crear un ciclo para moverse entre las entradas de la lista.
"""

# Inicialicemos los valores que contendrá la lista:
lista = [1,3,0,-9,-10]

mayor = lista[0]
for i in lista:
    if mayor < i:
        mayor = i
    
print("El valor más alto en la lista es: " + str(mayor))



"""
Ejercicio 4:

Escribe un programa en el que se cuenta el número de veces en que aparece la letra ‘a’ en la cadena ‘bananas’.

El algoritmo consiste en que cada que se cuente en una letra a en la cadena de texto, entonces una variable auxiliar, inicializada en cero, aumentará en una unidad. Para esto, crearemos una lista que contenga en cada entrada una letra o caracter de la cadena de texto. Luego, compararemos cada entrada de la lista con el string 'a' y en caso de ser iguales, aumentará en una unidad la variable auxiliar.
"""

# Crearemos una cadena de texto arbitraria
texto = "bananas"

# Inicialicemos el contador en 0:
contador = 0

for i in list(texto):
    if i == "a":
        contador += 1
print("La letra a aparece " + str(contador) + " veces en el texto " + str(texto))



"""
Ejercicio 5:

Escribe una función que calcula el valor factorial de cualquier número entero.

Consideremos que dado un número entero, para calcular su factorial tendremos que restarle una unidad sucesivamente hasta llegar al número 0.

El algoritmo verificará primero que el número no tenga parte decimal distinta de cero para que se obtenga el factorail conocido o usual. Además, dada la estructura del algoritmo, se aplicará por casos: Cuando el número es igual a cero y cuando el número es mayor o igual a uno. Si es igual a cero, se imprimirá que 0!=1; sin embargo, cuando el número es mayor o igual a uno, se multiplicará igualará a sí mismo multiplicador por la suma de la unidad más el iterador, donde este iterador aumentará desde cero hasta una canitdad menor al número del que interesa obtener el factorial, pero una unidad menor.
"""
x = 6

factorial = 1 # Ya que no afecta la multiplicación independientemente del valor de x.
residuo = x%1 # Ya que nos interesa comparar la parte decimal.

if residuo == 0:
    if x == 0:
        print("0! = 1")

    elif x >= 1:
        for i in range(x): # Empezar el ciclo después de x = 1 para i
            factorial = factorial*(1+i)
        print(str(x) + "! = " + str(factorial))

    else:
        print("El número es negativo por lo cual no se calculará su factorial.")
        
else:
    print("El número no es entero.")