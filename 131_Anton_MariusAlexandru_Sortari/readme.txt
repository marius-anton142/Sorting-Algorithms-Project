Merge Sort:

Este un algoritm de sortare de tipul divide et impera.
Time complexity-ul este O(nlogn).
Functioneaza prin impartirea listei in jumatati din ce in ce mai mici si interschimbarea elementelor in ordine.

Quick Sort:

Este un algoritm de sortare de tipul divide et impera.
Time complexity-ul este O(nlogn).
Functioneaza prin selectarea unui element pivot si mutarea numerelor mai mici decat acesta in stanga lui, si a celor mai mari in dreapta, dupa care aceeasi operatie se aplica pentru ambele jumatati si tot asa.
Pivotul poate fi ales ca primul sau ca ultimul element, dar, in acest caz, worst case scenario are loc atunci cand vectorul e sortat, respectiv sortat si inversat. In acest caz, time complexity-ul este O(n^2). O varianta mai buna este alegerea pivotului ca mijloc al vectorului, dar varianta pe care am implementat-o urmareste alegerea pivotului ca un element random din vector de fiecare data, pentru a reduce cat de mult posibil frecventa worst case scenario-ului.

Counting Sort:

Este cel mai eficient pentru vectori de 100000 de elemente maxim, cu complexitate liniara in timp. 
Sunt numarate elementele si puse intr-un vector de frecventa, dupa care sunt ordonate intr-un alt vector.

Radix Sort:

Este o varianta asemanatoare cu counting sortul pentru liste cu mai mult de 1000000 de elemente. In varianta implementata, este aleasa mai intai most significant digit al numerelor, iar acestea sunt sortate in functie de aceasta si puse in "bucket"-uri, dupa care sunt alese urmatoarele cifre si tot asa pana la least significant digit. Complexitatea este de O(nd), unde d este numarul de cifre din cel mai mare numar al vectorului.

Shell Sort:

Este o varianta generalizata a insertion sortului, prin care elementele sunt h-sortate treptat, unde h este gap-ul care este micsorat constant pana ajunge la 1.
Complexitatea in timp este O(nlogn), dar varianta pe care am implementat-o alege n/2 gap-ul initial si il imparte constant la 2, avand o complexitate de O(n^2).

Timpii observati pentru mai multe date de intrare (masurati in secunde):

merge_sort N = 1000 Max = 10000000 0.004021883010864258 True
merge_sort N = 10000 Max = 1000 0.0523989200592041 True
merge_sort N = 100 Max = 10000000 0.0 True
merge_sort N = 10 Max = 1000 0.0 True
merge_sort N = 100000 Max = 1000000 0.6423153877258301 True
quick_sort N = 1000 Max = 10000000 0.003968238830566406 True
quick_sort N = 10000 Max = 1000 0.03390908241271973 True
quick_sort N = 100 Max = 10000000 0.0 True
quick_sort N = 10 Max = 1000 0.0 True
quick_sort N = 100000 Max = 1000000 0.34580063819885254 True
counting_sort N = 1000 Max = 10000000 2.364250898361206 True
counting_sort N = 10000 Max = 1000 0.0498347282409668 True
counting_sort N = 100 Max = 10000000 2.3375320434570312 True
counting_sort N = 10 Max = 1000 0.04886746406555176 True
counting_sort N = 100000 Max = 1000000 0.30515241622924805 True
shell_sort N = 1000 Max = 10000000 0.10768318176269531 True
shell_sort N = 10000 Max = 1000 15.153645277023315 True
shell_sort N = 100 Max = 10000000 0.000997304916381836 True
shell_sort N = 10 Max = 1000 0.0 True
radix_sort N = 100 Max = 10000000 0.06086850166320801 True
radix_sort N = 10 Max = 1000 110.8162169456482 True

Pentru N = 100000 Max = 1000000 pentru shell sort si pentru N = 1000 Max = 10000000, N = 10000 Max = 1000, N = 100 Max = 10000000 pentru radix sort, algoritmii dureaza prea mult pentru a returna un rezultat, asa ca procesul a fost abandonat.