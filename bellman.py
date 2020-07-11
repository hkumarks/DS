import sys

def bellmanFord(g,dist,v):
    for n in range(v-1):
        for u,v,w in g:
            if dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
                    
    for u,v,w in g:
        if dist[u]+w<dist[v]:
            return 'The graph contains cycle'
                
    return dist   

v,e=input().split()
v,e=int(v),int(e)
a=[int(i) for i in input().split()]

g=[]
for i in range(e):
    g.append(a[0:3])
    for z in range(3):
        a.remove(a[0])
        
dist=[sys.maxsize]*v
dist[0]=0
print(bellmanFord(g,dist,v))
    

            