def mergesort(arr,low,high):
    if low<high:
        mid=(low+high)//2

        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    n1=mid-low+1
    n2=high-mid

    L=[None]*n1
    R=[None]*n2

    for i in range(n1):
        L[i]=arr[low+i]

    for j in range(n2):
        R[j]=arr[mid+1+j]

    i=0
    j=0
    k=low

    while i<n1 and j<n2:
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1

    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1

a=[3,8,0,1,0]
mergesort(a,0,4)
print(*a)                                          