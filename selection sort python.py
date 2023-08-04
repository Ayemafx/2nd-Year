def selection_Sort(array):
    swap = 0
    comparison = 0
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            comparison += 1
            if array[min_index] > array[j]:
                min_index = j
        swap += 1
        array[i], array[min_index] = array[min_index], array[i]
    return swap, comparison


sort = ['P', 'Y', 'T', 'H', 'O', 'N']
print(selection_Sort(sort))
print("Sorted array")
print(sort)