def mergeSort(A, left, right):
    if left < right:
        mid = (right+left)//2

        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)

        merge(A, left, mid, right)


def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = 0

    temp = [0]*100

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i += 1
            k += 1
        else:
            temp[k] = A[j]
            j += 1
            k += 1
    while i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = A[j]
        j += 1
        k += 1

    k = 0
    for i in range(left, right+1):
        A[i] = temp[k]
        i += 1
        k += 1


n = int(input("enter the number elements for array: "))
A = []

for i in range(n):
    number = int(input(f"Enter number: "))
    A.append(number)

print("Unsorted Array: ", A)

mergeSort(A, 0, n-1)

print("Sorted Array: ", A)
