import tkinter as tk
import time
import matplotlib.pyplot as plt

def fibonacci (n):
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_dp(n):
    if n <= 1:
        return n
    F = [0] * (n + 1)

    F[0] = 0
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i -1] + F[i -2]

    return F[n]

def compare():
    start = inicio.get()
    increment = incremento.get()
    end = final.get()

    values = list(range(start, end + 1, increment))
    times_f = []
    times_fdp = []
    text = ""

    for n in values:

        start_f = time.perf_counter()
        fibonacci(n)
        end_f = time.perf_counter()   
        t_f = end_f - start_f

        start_fdp = time.perf_counter()
        fibonacci_dp(n)
        end_fdp = time.perf_counter()   
        t_dp = end_fdp - start_fdp

        times_f.append(t_f)
        times_fdp.append(t_dp)
  
    lbl_list_sort.config(text=text)
    plt.figure(num="Grafica", clear=True)
    plt.plot(values, times_f, marker="o", label="Fibonacci")
    plt.plot(values, times_fdp, marker="o", label="Fibonacci_dp")

    plt.title("Grafica")
    plt.xlabel("Fibonacci")
    plt.ylabel("Tiempos (s)")
    plt.grid()
    plt.legend()

    plt.show()
    
root = tk.Tk()
root.title("Comparador de fibonacci")
root.geometry("600x800")

lbl_min = tk.Label(root, text="Inicio:")
lbl_min.pack(pady=30)
inicio = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, length=200)
inicio.pack(pady=10)
lbl_increase = tk.Label(root, text="Incremento:")
lbl_increase.pack(pady=30)
incremento = tk.Scale(root, from_=5, to=10, orient=tk.HORIZONTAL, length=200)
incremento.pack(pady=10)
lbl_max = tk.Label(root, text="Final:")
lbl_max.pack(pady=30)
final = tk.Scale(root, from_=10, to=60, orient=tk.HORIZONTAL, length=500)
final.pack(pady=10)
boton_sort = tk.Button(root, text="Graficar", command=compare)
boton_sort.pack(pady=1)
lbl_list_sort = tk.Label(root, text="")
lbl_list_sort.pack(pady=30)

root.mainloop()