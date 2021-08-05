def binary_search(list_sort, size, targer):
    low = 0
    high = size - 1
    while low <= high:
        mid = int((low + high) / 2)
        if targer == list_sort[mid]:
            return mid
        elif targer > list_sort[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1