from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph,x,y):
  queue=deque()
  queue.append((x,y))
  graph[x][y]=0
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or ny<0 or nx>=m or ny>=n:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=0
        queue.append((nx,ny))

for _ in range(int(input())):
  m,n,k=map(int,input().split())
  graph=[[0]*n for _ in range(m)]
  cnt=0
  for _ in range(k):
    a,b=map(int,input().split())
    graph[a][b]=1
  
  for i in range(m):
    for j in range(n):
      if graph[i][j]==1:
        bfs(graph,i,j)
        cnt+=1
  print(cnt)