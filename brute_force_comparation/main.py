import matplotlib.pyplot as plt
import json

with open("results.json") as f:
    results = json.load(f)

sizes = results["sizes"]
for name in ["bubble", "exchange", "gnome", "insertion", "selection", "stooge"]:
    plt.plot(sizes, results[name], marker="o", label=name)

plt.title("Grafica")
plt.xlabel("Algoritmo (n)")
plt.ylabel("Tiempos (s)")
plt.grid()
plt.legend()

plt.show()


