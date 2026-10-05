# Algorithm Analysis — Python

> **Work in progress.**

School project for the **Algorithm Analysis** course (CUCEI). The repository collects the class activities and projects, where algorithms are implemented in **Python** and their execution times are measured and plotted to compare them against their theoretical complexity.

## Goal

Implement classic algorithms and compare them empirically: generate inputs of increasing size, time each algorithm and plot the results to see how they grow with `n`.

## Structure

The repository is split into two parts:

- **`Activities/`**: class assignments. Each file is an independent activity, from Python basics to algorithm comparisons with a GUI.
- **`brute_force_comparation/`**: the brute force project. It benchmarks six brute force sorting algorithms on the same inputs and plots their times.

```
.
├── Activities/                       # Class activities
│   ├── 01_condicional.py             # Conditionals
│   ├── 02_for.py                     # For loops
│   ├── 03_bubble_sort.py             # Bubble Sort
│   ├── 04_gui.py                     # First Tkinter GUI
│   ├── 05_generador.py               # Random list generator
│   ├── 06_graph.py                   # First Matplotlib plot
│   ├── 07_bubble_vs_slection.py      # Bubble vs Selection Sort (GUI + plot)
│   ├── 08_pseudocodigo_monedas.txt   # Coin problem pseudocode
│   └── 09_fibonacci.py               # Recursive vs DP Fibonacci (GUI + plot)
└── brute_force_comparation/          # Brute force sorting project
    ├── benchmark.py                  # Generates inputs, times each sort, saves results.json
    ├── main.py                       # Reads results.json and plots the times
    └── sorts/                        # One file per sorting algorithm
```

## Algorithms

Each algorithm, with the file where it is implemented and its time complexity:

| Algorithm | File | Complexity | Notes |
|-----------|------|------------|-------|
| Bubble Sort | `sorts/bubble_sort.py`, `Activities/03`, `07` | O(n²) | Swaps adjacent pairs; the largest element "bubbles" to the end on each pass. |
| Selection Sort | `sorts/selection_sort.py`, `Activities/07` | O(n²) | Finds the minimum of the unsorted part and puts it in place. |
| Exchange Sort | `sorts/exchange_sort.py` | O(n²) | Compares each element with every later one and swaps immediately. |
| Insertion Sort | `sorts/insertion_sort.py` | O(n²) | Shifts larger elements to the right and inserts the key in its position. |
| Gnome Sort | `sorts/gnome_sort.py` | O(n²) | Moves forward while in order; otherwise swaps and steps back. |
| Stooge Sort | `sorts/stooge_sort_rec.py` | O(n^2.71) | Recursively sorts the first 2/3, the last 2/3 and the first 2/3 again. |
| Fibonacci (recursive) | `Activities/09_fibonacci.py` | O(2ⁿ) | Naive recursion; recomputes the same subproblems. |
| Fibonacci (DP) | `Activities/09_fibonacci.py` | O(n) | Bottom-up table; each value is computed only once. |
| Coin problem | `Activities/08_pseudocodigo_monedas.txt` | O(n) | DP: `f(n) = max(Cₙ + f(n−2), f(n−1))`, then backtracks to get the chosen coins. |

## Tools

- **Language:** Python 3
- **Libraries:** Matplotlib (plots), Tkinter (GUIs)

## Author

[@Rxjaz](https://github.com/Rxjaz) — Student at CUCEI, Universidad de Guadalajara.

---

*Academic project.*