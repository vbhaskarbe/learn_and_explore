#
## 26. Implement few sorting algorithms : Bubble, Quick, Insertion, Merge 
#

## Bubble sort
def bubble_sort( ulist):
    length = len( ulist)
    for flx in range(length):
        for fly in range(length - flx - 1):
            if ulist[fly] > ulist[fly + 1]:
                ulist[fly], ulist[fly + 1] = ulist[fly + 1], ulist[fly]
    print("The Bubble sorted list in ASCending order is    : ", ulist)

## Quick sort is also known as Partition Exchange sort
def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j],array[i]
    array[i + 1], array[high] = array[high], array[i +1]
    return (i + 1)

## Quick sort algorithm
def quick_sort( unsorted_list, low, high):
    if low < high:
        pi = partition( unsorted_list, low, high)
        quick_sort( unsorted_list, low, pi - 1)
        quick_sort( unsorted_list, pi + 1, high)

## Insertion sort
def insertion_sort( unsorted_list):
    for index in range( 1, len(unsorted_list)):
        key = unsorted_list[index]
        jindex = index - 1
        while jindex >= 0 and key < unsorted_list[jindex]:
            unsorted_list[jindex + 1] = unsorted_list[jindex]
            jindex -= 1
        unsorted_list[jindex + 1] = key
    print("The Insertion sorted list in ASCending order is :", unsorted_list)

# Merge sort
def merge_list(alist, start, mid, end):
    left  = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

def merge_sort( alist, sort, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)

if __name__ == '__main__':
    import time

    ulist = [ 10, 30, 50, 70, 40, 20, 60, 90, 80 ]
    print("The list of unordered elements are              : ", ulist) 

    start = time.time()
    bubble_sort( ulist)
    print("Execution time for Bubble sort method is        : %s sec" % (time.time() - start))
    
    start = time.time()
    quick_sort( ulist, 0, len(ulist) - 1)
    print("The Quick sorted list in ASCending order is     : ", ulist)
    print("Execution time for Quick sort method is         : %s sec" % (time.time() - start))

    start = time.time()
    insertion_sort( ulist)
    print("Execution time for Insertion sort method is     : %s sec" % (time.time() - start))

    start = time.time()
    merge_sort( ulist, 0, len(ulist))
    print("The Merge sorted list in ASCending order is     : ", ulist)
    print("Execution time for Merge sort method is         : %s sec" % (time.time() - start))


