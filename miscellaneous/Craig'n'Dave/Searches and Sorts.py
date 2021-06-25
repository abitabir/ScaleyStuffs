# linear search

lst1 = [8, 6, 9, 0]
searchingFor = 0


def LinearSearch(lst, searchingFor):
    pointer = 0
    while pointer < len(lst) and (lst[pointer] != searchingFor):
        pointer += 1
    if pointer >= len(lst):
        return ("item is not in the list")
    else:
        return ("item is at location %d" % pointer)


print(LinearSearch(lst1, searchingFor))


# binary search

def BinarySearch(lst, searchingFor):
    lowerBound = 0
    upperBound = len(lst) - 1
    found = False

    while (found == False) and (lowerBound <= upperBound):
        midPoint = round((lowerBound + upperBound) / 2)
        if lst[midPoint] == searchingFor:
            found = True
        elif lst[midPoint] < searchingFor:
            lowerBound = midPoint + 1
        else:
            upperBound = midPoint - 1

    if found == True:
        return ("item %d found at %d" % (searchingFor, midPoint))
    else:
        return ("item %d is not in list" % searchingFor)


print(BinarySearch([1, 54, 7687, 85784, 4857435, 47586439], 85784))

unsortedList = [43, 548, 7, 39, 97, 458, 3, 59, 78, 9]


# bubble sort

def BubbleSort(data):
    swapMade = True
    while swapMade == True:  # loop ends when swapMade is set to False in final check over data
        swapMade = False
        for index in range(len(data) - 1):
            if data[index] > data[index + 1]:
                copy = data[index]
                data[index] = data[index + 1]
                data[index + 1] = copy
                swapMade = True
    return (data)


print(BubbleSort(unsortedList))


# insertion sort

def InsertionSort(sortingList):
    for i in range(1, len(sortingList)):
        current = sortingList[i]
        while sortingList[i - 1] > current and i > 0:
            sortingList[i], sortingList[i + 1
                                        ] = sortingList[i], sortingList[i + 1]
            i = i - 1
    return (sortingList)


print(InsertionSort(unsortedList))

def insertion_sort(array):

    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue


def SplitList(arr, arrLeft, arrRight):
    middle = len(arr)/2
    pointerLeft = 0
    while pointerLeft != middle:
        arrLeft[pointerLeft] = arr[pointerLeft]
        pointerLeft += 1
    pointerRight = middle
    while pointerRight != len(arr):
        arrRight[pointerRight] = arr[pointerRight]
        pointerRight += 1

def MergeTwoLists(arr1, arr2):
    arr3 = []
    pointer1 = 0
    pointer2 = 0
    pointer3 = 0
    while pointer3 < len(arr1) + len(arr2) + 1:
        if arr1[pointer1] < arr2[pointer2]:
            arr3[pointer3] = arr1[pointer1]
            pointer1 += 1
        else:
            arr3[pointer3] = arr2[pointer2]
            pointer2 += 1
        pointer3 += 1
    return(arr3)



def MergeSort(arr):
    if len(arr) == 0:
        return(arr)
    arrLeftHalf = MergeSort(arrLeftHalf)
    arrRightHalf = MergeSort(arrRightHalf)
    SplitList(arr, arrLeftHalf, arrRightHalf)
    return(MergeTwoLists(arrLeftHalf, arrRightHalf))


print(MergeSort([6, 7, 49, 29, 70 , 595, 634, 45279348, 9695, 7, 8]))


def quicksort(arr, begin, end):
    if end - begin > 1:
        p = partition(arr, begin, end)
        quicksort(arr, begin, p)
        quicksort(arr, p + 1, end)


def partition(arr, begin, end):
    pivot = arr[begin]
    i = begin + 1
    j = end - 1

    while True:
        while (i <= j and arr[i] <= pivot):
            i = i + 1
        while (i <= j and arr[j] >= pivot):
            j = j - 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[begin], arr[j] = arr[j], arr[begin]
            return j


arr = input('Enter the list of numbers to be Sorted: ').split()
arr = [int(x) for x in arr]
quicksort(arr, 0, len(arr))
print('Sorted list: ', end='')