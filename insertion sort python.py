def insertionSort(array):
    swap = 0
    comparison = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            comparison += 1
            array[j + 1] = array[j]
            swap += 1
            j -= 1
        array[j + 1] = key


sort = ['P', 'Y', 'T', 'H', 'O', 'N']
insertionSort(sort)
print("Sorted Aray")
print(sort)

