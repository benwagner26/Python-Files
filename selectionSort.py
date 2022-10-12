
def selectionSort(list):

    indexing_length = range(0, len(list)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list)):
            if list[j] < list[min_value]:
                min_value=j

        if min_value != i:
            list[min_value], list[i] = list[i], list[min_value]

    
    return list



print(selectionSort([43,23,55,3,43,3,22,1,2]))