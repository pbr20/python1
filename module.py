import os
from DSA.sorting.BubbleSort import bubble_sort as bubble
from all_functions.RGB import rgb_color_gen

n = int(input("Enter number of elements: "))
A = []

for i in range(n):
    number = int(input())
    A.append(number)

print("Unsorted Array: ", A)
bubble(A)
print("Sorted Array: ", A)

# builtin_module

print(os.getcwd())
print(rgb_color_gen())
