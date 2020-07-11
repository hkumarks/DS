def heapify(arr,n,i):
    largest=i
    lc=2*i+1
    rc=2*i+2

    if lc<n and arr[lc]>arr[largest]:
        largest=lc

    if rc<n and arr[rc]>arr[largest]:
        largest=rc

    if largest is not i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)

def heapsort(arr,n,i):
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,-1,-1):
        arr[i],a[0]=a[0],arr[i]
        heapify(arr,i,0)

a=[3,8,0,1,0]
heapsort(a,5,0)
print(*a)                                 
