
# To sort array of elements using quick sort.
def quick_sort(low,high):
    if(low>=high ):
        return

    pivot = arr[low]
    index = low

    for i in range(low,high):
        if(arr[i]<pivot):
            arr[i],arr[index+1] = arr[index+1] , arr[i]
            index+=1
        else:
            pass
    print(arr)
    arr[low],arr[index] = arr[index] , arr[low]

    quick_sort(low,index)
    quick_sort(index+1,high)

arr = [1, 4, 10, 11, 20, 30]

quick_sort( 0,len(arr) )
print(arr)
