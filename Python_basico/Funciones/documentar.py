#Docstring
#__doc__(Módulos, Clases, Métodos y Funciones)
def suma(numero_1, numero_2):

    """
    La función suma 2 números enteros.

    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parametros.

    TODO: 
    *
    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300

    python -m doctest documentar.py se utiliza para ver que no haya errores
    """


    return numero_1 + numero_2

def resta(numero_1, numero_2):
    """
    >>> resta(100,200)
    -100
    """
    return numero_1 - numero_2