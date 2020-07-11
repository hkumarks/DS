def partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)

        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

a=[3,8,0,1,0]
quicksort(a,0,4)
print(*a)        
