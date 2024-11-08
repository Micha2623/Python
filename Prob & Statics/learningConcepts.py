# create a program that receives a list of data and calculates all the things (equations) in statistics.
from header import Functions
import math

f = Functions()
# f.d_entry()
frequency = f.frec()
frequency = dict(sorted(frequency.items()))
f.x = int(len(f.data))

lista_ordenada = list(map(float, f.data))
lista_ordenada.sort()

print(f"\n\nThe Statistics of the {f.tittle} are: ")
print("------------------------------------------------------------------")
print(f"Qty of data: {f.x}")
print("------------------------------------------------------------------")
print(f"Ordered list: {lista_ordenada}")
print("------------------------------------------------------------------")
print(f"Summation: {sum(lista_ordenada)}")
print("------------------------------------------------------------------")

if f.x % 2 == 0:
    median = (f.data[f.x // 2 - 1] + f.data[f.x // 2]) / 2
    print(f"Median: {median}")
elif f.x % 2 != 0:
    median = f.data[f.x // 2]
    print(f"Median: {median}")

print("------------------------------------------------------------------")

average = sum(lista_ordenada) / f.x if f.x > 0 else 0
print(f"Average: {average:.2f} {f.tittle}")

print("------------------------------------------------------------------")

mod = []
first_value = dict(sorted(frequency.items(), key=lambda item: item[1]))
for values in frequency:
    mode = frequency.get(values)
    mod.append(mode)
mod.sort(reverse=True)
first_value = list(first_value.keys())
print(f"Mode {first_value[-1]} : {mod[0]}")

print("------------------------------------------------------------------")

print("Frequency: ")
frec_sorted = dict(sorted(frequency.items()))
for key, value in frec_sorted.items():
    print(f"{key} : {value}")

print("------------------------------------------------------------------")
print("Cumulative absolute frequency: ")
cumulatedSum = 0
cumulatedFrec = {}
for key in sorted(frec_sorted.keys()):
    cumulatedSum += frec_sorted[key]
    cumulatedFrec[key] = cumulatedSum
for key, value in cumulatedFrec.items():
    print(f"{key} : {value}")

print("------------------------------------------------------------------")
print("Relative frequency: ")
relative_frec = {}
for key in frec_sorted.keys():
    relative_frec[key] = frec_sorted[key] / f.x
    print(f"{key} : {relative_frec[key]:.2f}")

print("------------------------------------------------------------------")
print("Porcentages: ")
porcentages = {}
for key in relative_frec.keys():
    porcentages[key] = relative_frec[key] * 100
    print(f"{key} : {porcentages[key]:.2f}%")
