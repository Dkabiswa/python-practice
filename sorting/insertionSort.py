def insertion_sort(list_a):
    for i in range(len(list_a)):
        current_number = list_a[i]
        while i > 0 and current_number < list_a[i-1]:
            list_a[i] = list_a[i-1]
            i -=1
        list_a[i] = current_number

arr = [2, 8, 14, 21, 10, 4, 1]
print(f"array before sort {arr}")
insertion_sort(arr)
print(f'sorted array is {arr}')