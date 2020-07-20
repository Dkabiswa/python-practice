def selection_sort(list_a):
    n = len(list_a)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if list_a[minimum] > list_a[j]:
                minimum = j
        list_a[minimum], list_a[i] = list_a[i], list_a[minimum]

arr = [2, 8, 14, 21, 10, 4, 1]
print(f"array before sort {arr}")
selection_sort(arr)
print(f'sorted array is {arr}')