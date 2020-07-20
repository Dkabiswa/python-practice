# def quick_sort(list_a):
#     if len(list_a) <= 1:
#         return list_a
#     else:
#         pivot = list_a.pop()
#     less_than = []
#     greater_than = []

#     for item in list_a:
#         if item > pivot:
#             greater_than.append(item)
#         else:
#             less_than.append(item)

#     return quick_sort(less_than) + [pivot] + quick_sort(greater_than)


# arr = [2, 8, 14, 21, 10, 4, 1]
# print(f"array before sort {arr}")
# quick_sort(arr)
# print(f'sorted array is {arr}')