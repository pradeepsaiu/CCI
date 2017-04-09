def merge_sort(array):
    sort(array,0,len(array)-1)

def sort(array,left,right):
    if(left>=right):
        return

    middle = (left +right )/2
    sort(array,left,middle)
    sort(array,middle+1,right)
    merge(array,left,middle,right)

def merge(array,left,middle,right):
    temp = [0]*(right-left+1)
    left_index = left
    right_index = middle+1
    count = 0
    flag = 1
    print(array,left,middle,right)
    while(left_index<=middle and right_index<=right ):
        print('hi')
        if(array[left_index] < array[right_index]):
            temp[count]= array[left_index]
            count+=1;left_index+=1;flag=1;
        else:
            temp[count]=array[right_index]
            count+=1;right_index+=1;flag =0;
    #copy the remaining elements from whichever array remains.
    if(left_index>middle):
        while(right_index<=right):
            print("There");
            temp[count]=array[right_index]
            count+=1;right_index+=1;
    elif(right_index>right):
        while(left_index<=middle):
            print('here')
            temp[count]= array[left_index]
            count+=1;left_index+=1;flag=1;

    count=0
    #copy temporary array back to the original array
    while(left<=right):
        array[left] =temp[count]
        count+=1;left+=1;
    print(array)
    print('\n')

data = [12,22,4,15,8,122,159,100,11]
merge_sort(data)
print(data)
