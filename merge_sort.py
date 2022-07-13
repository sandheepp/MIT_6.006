def merge_sort(array, beg=0, end= None):
    #if in anyway end is not mentioend, set it as the length of the array sent
    if end is None: end = len(array)
    
    # If length of array is atleast one
    if end-beg>1:
        # find the mid area
        mid = (beg+end+1)//2
        merge_sort(array, beg, mid)
        merge_sort(array, mid, end)
        L, R = array[beg:mid], array[mid:end]

        #merge the L and R if the array
        merge(L,R,array,len(L), len(R), beg, end)
        return array

def merge(L,R,array,i, j, beg, end):
    if beg<end:
        if j<=0 or (i>0 and L[i-1]>R[j-1]):
            array[end-1] = L[i-1]
            i = i-1
        else:
            array[end-1] = R[j-1]
            j = j-1
        merge(L,R,array,i,j,beg, end-1)


if __name__=="__main__":
    array = [ 6,9, 5,3, 323, 56]
    sorted_array = merge_sort(array,0, len(array))
    print("Sorted:",sorted_array)