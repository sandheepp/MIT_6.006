'''
Insertion sort:
1. Loop through array
2. place the current element wrt to the sorted list to the left of it
'''


def insertion_sort(array, length):
    for i in range(length):
        j = i-1
        key = array[i]
        while key < array[j] and j>=0:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

if __name__=="__main__":
    array = [ 6,9, 5,3, 323, 56]
    sorted_array = insertion_sort(array, len(array))
    print("Sorted:",sorted_array)