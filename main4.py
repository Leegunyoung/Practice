INF=int(1e9)
n,m = map(int, input().split())
s,a,t=map(int,input().split())
edges=[]
dist=[INF]*(n+1)   


for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u,v,w))

def bf(start, end):  
        dist[start]=0
        for i in range(n):
            for j in range(m):
                node=edges[j][0]
                next_node=edges[j][1]
                cost=edges[j][2]
                if(dist[node] !=INF  and dist[next_node]>dist[node]+cost):
                    dist[next_node]=dist[node]+cost
        result=dist[end]
        return result   

s1=bf(s,a)    #0,2
dist=[INF]*(n+1)
s2=bf(a,t)    #2,3
print(s1+s2)

    
    
                
    