n,m,k=map(int,input().split())
g=[]
for _ in range(n):
  tmp=list(map(int,input()))
  g.append(tmp)

visit=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]

from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(sx,sy):
  q=deque()
  q.append((sx,sy,0))
  visit[sy][sx][0]=1
  while q:
    x,y,z=q.popleft()
    if x==m-1 and y==n-1:
      return visit[y][x][z]

    for i in range(4):
      nx,ny=x+dx[i],y+dy[i]
      if nx<0 or nx>=m or ny < 0 or ny>=n:
        continue

      if g[ny][nx] == 1 and z < k and visit[ny][nx][z+1]==0:
        visit[ny][nx][z+1] = visit[y][x][z]+1
        q.append((nx,ny,z+1))
      elif g[ny][nx]==0 and visit[ny][nx][z]==0:
        visit[ny][nx][z]= visit[y][x][z]+1
        q.append((nx,ny,z))
  return -1

print(bfs(0,0))
