import heapq
q=[]

n,m=map(int,input().split())
t,delay,x,b=map(int,input().split())
g=[[] for _ in range(n)]

INF=int(1e9)
visit=[[INF for _ in range(m)] for _ in range(n)]
for i in range(n):
  tmp=input()
  for j,k in enumerate(tmp):
    g[i].append(k)
    if k=='*':
      heapq.heappush(q,(0,i,j))
      visit[i][j]=0
  
dx=[1,-1,0,0]
dy=[0,0,1,-1]

while q:
  dist,py,px=heapq.heappop(q)
  for i in range(4):
    x=px+dx[i]
    y=py+dy[i]
    if x<0 or x>=m or y<0 or y>=n:
      continue
    if g[y][x]=='*':
      continue
    if g[y][x]=='.':
      if visit[y][x]>dist+1:
        visit[y][x]=dist+1
        heapq.heappush(q,(dist+1,y,x))
    if g[y][x]=='#':
      if visit[y][x]>dist+delay+1:
        visit[y][x]=dist+delay+1
        heapq.heappush(q,(dist+delay+1,y,x))
a=False
for i in range(n):
  for j in range(m):
    if visit[i][j]>t:
      print(i+1,j+1)
      a=True
if not a:
  print(-1)