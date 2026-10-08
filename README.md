# Algorithm Analysis — Python

> **Work in progress.**

School project for the **Algorithm Analysis** course (CUCEI). The repository collects the class activities and projects, where algorithms are implemented in **Python** and their execution times are measured and plotted to compare them against their theoretical complexity.

## Goal

Implement classic algorithms and compare them empirically: generate inputs of increasing size, time each algorithm and plot the results to see how they grow with `n`.

## Structure

All the work lives in **`Activities/`**, one folder per activity, from Python basics to algorithm comparisons with a GUI and plots.

```
.
└── Activities/
    ├── 01_learning_python/           # Python basics
    │   ├── if.py                     # Conditionals
    │   ├── for.py                    # For loops
    │   ├── bubble_sort.py            # Bubble Sort
    │   ├── tkinter_gui.py            # First Tkinter GUI
    │   ├── generate_array.py         # Random list generator
    │   └── matplotlib.py             # First Matplotlib plot
    ├── 02_bubble_vs_sel/
    │   └── bubble_vs_slection.py     # Bubble vs Selection Sort (GUI + plot)
    ├── 03_brute_force/               # Brute force sorting project
    │   ├── benchmark.py              # Generates inputs, times each sort, saves results.json
    │   ├── main.py                   # Reads results.json and plots the times
    │   └── sorts/                    # One file per sorting algorithm
    ├── 05_coin_problem/
    │   ├── pseudocode_coin.txt       # Coin problem pseudocode
    │   └── coin.py                   # Coin problem implementation
    └── 06_fibonacci_dp/
        └── fibonacci.py              # Recursive vs DP Fibonacci (GUI + plot)
```

## Algorithms

Each algorithm, with the file where it is implemented and its time complexity:

| Algorithm | File | Complexity | Notes |
|-----------|------|------------|-------|
| Bubble Sort | `03_brute_force/sorts/bubble_sort.py`, `01_learning_python/bubble_sort.py`, `02_bubble_vs_sel` | O(n²) | Swaps adjacent pairs; the largest element "bubbles" to the end on each pass. |
| Selection Sort | `03_brute_force/sorts/selection_sort.py`, `02_bubble_vs_sel` | O(n²) | Finds the minimum of the unsorted part and puts it in place. |
| Exchange Sort | `03_brute_force/sorts/exchange_sort.py` | O(n²) | Compares each element with every later one and swaps immediately. |
| Insertion Sort | `03_brute_force/sorts/insertion_sort.py` | O(n²) | Shifts larger elements to the right and inserts the key in its position. |
| Gnome Sort | `03_brute_force/sorts/gnome_sort.py` | O(n²) | Moves forward while in order; otherwise swaps and steps back. |
| Stooge Sort | `03_brute_force/sorts/stooge_sort_rec.py` | O(n^2.71) | Recursively sorts the first 2/3, the last 2/3 and the first 2/3 again. |
| Fibonacci (recursive) | `06_fibonacci_dp/fibonacci.py` | O(2ⁿ) | Naive recursion; recomputes the same subproblems. |
| Fibonacci (DP) | `06_fibonacci_dp/fibonacci.py` | O(n) | Bottom-up table; each value is computed only once. |
| Coin problem | `05_coin_problem/` | O(n) | DP: `f(n) = max(Cₙ + f(n−2), f(n−1))`, then backtracks to get the chosen coins. |

## Tools

- **Language:** Python 3
- **Libraries:** Matplotlib (plots), Tkinter (GUIs)

## Author

[@Rxjaz](https://github.com/Rxjaz) — Student at CUCEI, Universidad de Guadalajara.

---

*Academic project.*
