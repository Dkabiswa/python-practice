def merge_sort(list_a):
    if len(list_a) > 1:
        mid = len(list_a)//2
        left_side = list_a[:mid]
        right_side = list_a[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                list_a[k] = left_side[i]
                i += 1
            else:
                list_a[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            list_a[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            list_a[k] = right_side[j]
            j += 1
            k += 1

arr = [2, 8, 14, 21, 10, 4, 0]
print(f"array before sort {arr}")
merge_sort(arr)
print(f'sorted array is {arr}')