n,k=map(int,input().split())
time=[0]*100001

from collections import deque
def bfs(s):
  q=deque()
  q.append(s)
  while q:
    p=q.popleft()
    if p==k:
      print(time[p])
      break
    for i in (p+1,p-1,2*p):
      if 0<=i<=100000 and not time[i]:
        time[i]=time[p]+1
        q.append(i)
    
bfs(n)