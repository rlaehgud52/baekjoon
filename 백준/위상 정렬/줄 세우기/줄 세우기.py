import sys
input=sys.stdin.readline
n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
cnt=[0]*(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  g[a].append(b)
  cnt[b]+=1
ans=[]

from collections import deque
q=deque()

for i in range(1,n+1):
  if cnt[i]==0:
    q.append(i)

while q:
    p=q.popleft()
    ans.append(p)
    for i in g[p]:
      cnt[i]-=1
      if cnt[i]==0:
            q.append(i)
      
print(*ans)
