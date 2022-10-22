




# Slices

from tkinter import N
from tracemalloc import DomainFilter


nombre = "Daniel"

reb1 = nombre[0:3]
reb2 = nombre[3:6]
reb3 = nombre[0:6:2]
reb4 = nombre[::]
reb5 = nombre[::-1]

print(reb1)
print(reb2)
print(reb3)
print(reb4)
print(reb5)