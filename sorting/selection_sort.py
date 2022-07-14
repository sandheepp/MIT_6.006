'''
Selection Sort:
1. Find biggest item
2. Swap it with the rightmost one
3. Repeat for the list for length-1
'''

def selection_sort(array, length):
    if length <1:
        print("returning", array)
        return array
    
    #loop or recursion can be used to find the largest element in a list
    max_item = array[0]
    location = 0
    for i in range(1, length):
        if array[i]> max_item:
            location = i
            max_item = array[i]
    

    array[location], array[length-1] = array[length-1], array[location]
    return selection_sort(array, length-1)


if __name__=="__main__":
    array = [ 6,9, 5,3, 323, 56]
    sorted_array = selection_sort(array, len(array))
    print("Sorted:",sorted_array)