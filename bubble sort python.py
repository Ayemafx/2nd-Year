def bubbleSort(array):
    swap = 0
    comparison = 0
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap += 1
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            comparison += 1
    return swap, comparison

sort = ['P', 'Y', 'T', 'H', 'O', 'N']
print(bubbleSort(sort))

print('Sorted Array in Ascending Order:')
print(sort)
