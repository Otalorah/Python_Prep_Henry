import random
# Se establecen las funciones en un contexto global


def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def son_primos(lista):

    lista_primos = list()

    if type(lista) != list:
        return "No es una lista de números"
    else:
        for i in lista:
            primo = es_primo(i)
            if primo:
                lista_primos.append(i)

    lista_primos.sort()

    return lista_primos


def repeticiones(lista):

    numeros = {}

    # Verificando si el parametro es un dato tipo lista
    if type(lista) != list:
        return "No es una lista de números"
    else:
        # Agregando los numeros de la lista a un diccionario para verificar el número de veces que se repite
        for num in lista:
            if str(num) in numeros:
                numeros[str(num)] += 1
            else:
                numeros[str(num)] = 1

        num_max_repeticiones = []
        num_repeticiones_anterior = 0
        num_max = 0

    # Filtrando los números por los números que tengan mayor número de repeticiones que el número anterior
        for n in numeros:
            if numeros[n] >= num_repeticiones_anterior:
                tupla = (n, numeros[n])
                num_max_repeticiones.append(tupla)
                num_repeticiones_anterior = numeros[n]
    # Filtrando el número que tenga más repeticiones y guardando la cantidad de repeticiones en num_max
            if numeros[n] >= num_max:
                num_max = numeros[n]

        numeros_max = list()

    # Verificando en la lista de los números con más repeticiones cual tiene el valor de num_max
        for n in range(len(num_max_repeticiones)):
            if num_max_repeticiones[n][1] == num_max:
                # Agregando los números que tengan el valor num_max a la lista numeros_max
                tupla = (num_max_repeticiones[n])
                numeros_max.append(tupla)
    # Creando un número entero aleatorio para escojer cualquier número que este en numeros_max
        n_random = random.randint(0, len(numeros_max)-1)
        return numeros_max[n_random]


def convertir_grados(n):
    # Celsius a Fahrenheit
    valorCF = (n*(9/5)) + 32
    texto = f" | {n}°C son {valorCF}°F  |"
    # Celsius a Kelvin
    valorCK = n + 273.15
    texto2 = f" | {n}°C son {valorCK}°K  |"
    # Fahrenheit a Kelvin
    valorFK = ((n - 32) * (5/9)) + 273.15
    texto3 = f" | {n}°F son {valorFK}°K  |"

    return [texto, texto2, texto3]


def factorial(n):
    if n > 1:
        n = n * factorial(n-1)
    return n


class Numeros():
    '''
     Numeros(int)
     Recibe un entero  
     Genera una lista con la cantidad de elementos igual al entero recibido
    '''

    def __init__(self, valor):
        self.valor = valor
        # A partir del valor ingresado se crea una lista
        self.lista = list()
        for i in range(valor):
            i = round(random.randint(0, i))
            self.lista.append(i)

    def lista_primos(self):
        primos = set(son_primos(self.lista))
        return list(primos)

    def valor_modal(self):
        return repeticiones(self.lista)

    def pasar_a_grados(self):
        texto = ""
        for n in convertir_grados(self.valor):
            texto += n
        return texto

    def _factorial(self):
        return factorial(self.valor)
