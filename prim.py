import sys

def findMin(key,mst):
    mini=sys.maxsize
    n=len(key)

    for i in range(n):
        if not mst[i] and key[i]<mini:
            mini=key[i]
            min_index=i
    return min_index        

def printmst(mat,parent):
    for i in range(1,len(parent)):
        print('{}--> {}, Cost={}'.format(parent[i],i,mat[i][parent[i]]))

def prim(mat,n):
    key=[sys.maxsize]*n
    parent=[0]*n
    mst=[False]*n

    parent[0]=-1
    key[0]=0

    for _ in range(n-1):
        i=findMin(key,mst)
        mst[i]=True

        for j in range(n):
            if mat[i][j] and not mst[j] and key[j]>mat[i][j]:
                key[j]=mat[i][j]
                parent[j]=i
    print(*parent)
    printmst(mat,parent)

a=[[0,2,0,6,0],[2,0,3,8,6],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
n=5

prim(a,n)