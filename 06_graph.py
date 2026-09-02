import matplotlib.pyplot as plt

n = [1, 2, 3, 4, 5]

algoritmo_1 = [0.001, 0.002, 0.003, 0.004, 0.005]
algoritmo_2 = [0.002, 0.008, 0.018, 0.032, 0.050]

plt.plot(n, algoritmo_1, marker="o", label="Algoritmo 1")
#plt.plot(n, algoritmo_2, marker="o", label="Algoritmo 1")
plt.scatter(n, algoritmo_2, marker="o", label="Algoritmo 1")

plt.title("Grafica")
plt.xlabel("Algoritmo (n)")
plt.ylabel("Tiempos (s)")
plt.grid()
plt.legend()

plt.show()