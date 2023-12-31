def merge(array, leftIndex, middleIndex, rightIndex):
    leftLen = middleIndex - leftIndex + 1
    rightLen = rightIndex - middleIndex

    L = [0 for _ in range(leftLen)]
    R = [0 for _ in range(rightLen)]

    for i in range(leftLen):
        L[i] = array[leftIndex + i]

    for j in range(rightLen):
        R[j] = array[middleIndex + 1 + j]

    i = 0
    j = 0
    k = leftIndex
    while(i < leftLen and j < rightLen):
        if(L[i] <= R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while(i < leftLen):
        array[k] = L[i]
        i += 1
        k += 1

    while(j < rightLen):
        array[k] = R[j]
        j += 1
        k += 1
    
def mergeSort(array, left, right):
    if(left < right):
        middle = (left + right) // 2
        mergeSort(array, left, middle)
        mergeSort(array, middle+1, right)
        merge(array, left, middle, right)