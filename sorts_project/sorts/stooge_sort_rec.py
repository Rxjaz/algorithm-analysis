'''
l (Low / Izquierda): Es el índice inicial (límite inferior) de la sublista actual.

h (High / Derecha): Es el índice final (límite superior) de la sublista actual.
Ejemplo de uso stooge_sort_rec(arr, 0, len(arr) - 1)
'''


def stooge_sort_rec(arr, l, h):
    if l >= h:
        return

    # Si el primer elemento es mayor que el último, intercambiar
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    # Si hay 3 o más elementos en el rango
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        # Aplicar fuerza bruta a los 3 tercios superpuestos
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3
        stooge_sort_rec(arr, l + t, h)       # Últimos 2/3
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3 de nuevo

def stooge_sort(lista):
    arr = lista.copy()
    stooge_sort_rec(arr, 0, len(arr) - 1)
    return arr