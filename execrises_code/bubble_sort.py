def bubble_sort(list_sort):
    for i in range(len(list_sort)):
        for j in range(len(list_sort) - i - 1):
            if list_sort[j] > list_sort[j + 1]:
                list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]
    return list_sort