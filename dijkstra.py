import sys

def findMin(dist,n,visited):
    min=sys.maxsize
    for i in range(n):
        if not visited[i] and min>dist[i]:
            min=dist[i]
            index=i
    return index        

def dijkstra(src, V, g):
    visited=[False]*V
    dist=[sys.maxsize]*V
    
    dist[src]=0
        
    for _ in range(V):
        index=findMin(dist,V,visited)
                
        visited[index]=True
        
        for i in range(V):
            if g[index][i]>0 and not visited[i] and dist[i]>dist[index]+g[index][i]:
                dist[i]=dist[index]+g[index][i]
    return dist       
