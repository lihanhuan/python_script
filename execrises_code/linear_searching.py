def linear_searching(list, size, target):
    for i in range(0, size):
        if (list[i] == target):
            return i;
    return -1;