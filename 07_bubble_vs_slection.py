import tkinter as tk
import random
import time
import matplotlib.pyplot as plt

arrays = []
times_bubble = []
times_selection = []
sizes = []

def generate_array():
    global arrays
    arrays = []

    start = int(inicio.get())
    increase = int(incremento.get())
    end = int(final.get())

    for i in range(start, end+1, increase):
        sublist = []
        for j in range(i):
            sublist.append(random.randint(1, end))
        arrays.append(sublist)

    text = ""
    for sublist in arrays:
        text = text + str(sublist)

    return text

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def click_generate():
    lbl_list.config(text=generate_array())

def click_sort():
    global times_bubble, times_selection, sizes
    times_bubble = []
    times_selection = []
    sizes = []

    text = ""
    for sublist in arrays:
        sublist_bubble = sublist.copy()
        sublist_selection = sublist.copy()

        start_time_bubble = time.perf_counter()
        bubble_sort(sublist_bubble)
        end_time_bubble = time.perf_counter()   
        elapsed_bubble = end_time_bubble - start_time_bubble

        start_time_selection = time.perf_counter()
        selection_sort(sublist_selection)
        end_time_selection = time.perf_counter()   
        elapsed_selection = end_time_selection - start_time_selection

        times_bubble.append(elapsed_bubble)
        sizes.append(len(sublist_bubble))   

        times_selection.append(elapsed_selection)
  
        #text = text + str(sublist) + " Tiempo: " + str(elapsed) + "\n"
    plt.figure(num="Grafica", clear=True)
    plt.plot(sizes, times_bubble, marker="o", label="Bubble")
    plt.plot(sizes, times_selection, marker="o", label="Selection")

    plt.title("Grafica")
    plt.xlabel("Algoritmo (n)")
    plt.ylabel("Tiempos (s)")
    plt.grid()
    plt.legend()

    plt.show()
    lbl_list_sort.config(text=text)

root = tk.Tk()
root.title("Generador de listas")
root.geometry("600x800")

lbl_min = tk.Label(root, text="Numero de elementos de la primera lista:")
lbl_min.pack(pady=30)
inicio = tk.Scale(root, from_=5, to=100, orient=tk.HORIZONTAL, length=200)
inicio.pack(pady=10)
lbl_increase = tk.Label(root, text="Incremento:")
lbl_increase.pack(pady=30)
incremento = tk.Scale(root, from_=5, to=100, orient=tk.HORIZONTAL, length=200)
incremento.pack(pady=10)
lbl_max = tk.Label(root, text="Numero de elementos de la ultima lista")
lbl_max.pack(pady=30)
final = tk.Scale(root, from_=100, to=10000, orient=tk.HORIZONTAL, length=500)
final.pack(pady=10)
boton_generate = tk.Button(root, text="Generar lista", command=click_generate)
boton_generate.pack(pady=1)
lbl_list = tk.Label(root, text="")
lbl_list.pack(pady=30)
boton_sort = tk.Button(root, text="Ordenar lista", command=click_sort)
boton_sort.pack(pady=1)
lbl_list_sort = tk.Label(root, text="")
lbl_list_sort.pack(pady=30)

root.mainloop()