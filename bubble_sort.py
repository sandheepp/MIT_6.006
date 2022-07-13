'''
Bubble sort:
1. Compare two elements
2. Move if the latter element is bigger
'''
def bubble_sort(array, length):
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__=="__main__":
    array = [ 6,9, 5,3, 323, 56]
    sorted_array = bubble_sort(array, len(array))
    print("Sorted:",sorted_array)