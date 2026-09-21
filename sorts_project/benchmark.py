import random
import time
import json

from sorts import bubble_sort as bub
from sorts import exchange_sort as exc
from sorts import gnome_sort as gno
from sorts import insertion_sort as ins
from sorts import selection_sort as sel
from sorts import stooge_sort_rec as sto

arrays = []

arrays_times = []
times_bubble = []
times_exchange = []
times_gnome = []
times_insertion = []
times_selection = []
times_stooge = []

def generate_array():

    arrays = []
    start = int(input("Inicio:")) 
    increment = int(input("Incremento: "))
    end = int(input("Final: "))

    for i in range(start, end+1, increment):
        sublist = []
        for j in range(i):
            sublist.append(random.randint(1, end))
        arrays.append(sublist)

    return arrays

arrays = generate_array()

for arr in arrays:

    arr_bubble = arr.copy()
    arr_exchange = arr.copy()
    arr_gnome= arr.copy()
    arr_insertion = arr.copy()
    arr_selection = arr.copy()
    arr_stooge = arr.copy()

    t_bub_ini=time.time()
    bubble_sorted = bub.bubble_sort(arr_bubble)
    t_bub_fin=time.time()
    times_bubble.append(t_bub_fin - t_bub_ini)

    t_exc_ini=time.time()
    exchange_sorted = exc.exchange_sort(arr_exchange)
    t_exc_fin=time.time()
    times_exchange.append(t_exc_fin - t_exc_ini)

    t_gno_ini=time.time()
    gnome_sorted = gno.gnome_sort(arr_gnome)
    t_gno_fin=time.time()
    times_gnome.append(t_gno_fin - t_gno_ini)

    t_ins_ini=time.time()
    insertion_sorted = ins.insertion_sort(arr_insertion)
    t_ins_fin=time.time()
    times_insertion.append(t_ins_fin - t_ins_ini)

    t_sel_ini=time.time()
    selection_sorted = sel.selection_sort(arr_selection)
    t_sel_fin=time.time()
    times_selection.append(t_sel_fin - t_sel_ini)

    t_sto_ini=time.time()
    stooge_sorted = sto.stooge_sort(arr_stooge)
    t_sto_fin=time.time()
    times_stooge.append(t_sto_fin - t_sto_ini)

    arrays_times.append(len(arr))

results = {
    "sizes": arrays_times,
    "bubble": times_bubble,
    "exchange": times_exchange,
    "gnome": times_gnome,
    "insertion": times_insertion,
    "selection": times_selection,
    "stooge": times_stooge
}

with open("results.json", "w") as f:
    json.dump(results, f)