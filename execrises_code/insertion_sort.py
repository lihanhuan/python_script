def insertion_sort(list_sort):
    for i in range(1, len(list_sort)):
        key = list_sort[i]
        j = i - 1
        while j >= 0 and key < list_sort[j]:
            list_sort[j + 1] = list_sort[j]
            j -= 1
            list_sort[j + 1] = key
    return list_sort