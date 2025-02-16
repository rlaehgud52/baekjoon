import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

v,e=map(int,input().split())
start_node=int(input())
g=[[] for _ in range(v+1)]
dis=[INF]*(v+1)
for _ in range(e):
  tmp=list(map(int,input().split()))
  g[tmp[0]].append((tmp[1],tmp[2]))

def di(s):
    q=[]
    heapq.heappush(q,(0,s)) 
    dis[s]=0

    while q:
      dist,c_nod=heapq.heappop(q)
      if dis[c_nod]<dist:
        continue
      for i in g[c_nod]:
        cost=dist+i[1]
        if cost<dis[i[0]]:
          dis[i[0]]=cost
          heapq.heappush(q,(cost,i[0]))

di(start_node)
for i in range(1,v+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])