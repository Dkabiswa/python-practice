def bubble_sort(list_a):
    n = len(list_a)
    for i in range(n-1):
        for j in range(n-i-1):
            if list_a[j+1] < list_a[j]:
                list_a[j+1], list_a[j] = list_a[j], list_a[j+1]

arr = [2, 8, 14, 21, 10, 4, 0]
print(f"array before sort {arr}")
bubble_sort(arr)
print(f'sorted array is {arr}') 