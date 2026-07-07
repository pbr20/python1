def bubble_sort(a_list):
    for i in range(len(a_list)-1):
        for j in range(len(a_list)-1-i):
            if (a_list[j] > a_list[j+1]):
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]


n = int(input("Enter the number of elements: "))
a_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a_list.append(element)

bubble_sort(a_list)
print("Sorted list:", a_list)

# https://csvistool.com/BubbleSort
