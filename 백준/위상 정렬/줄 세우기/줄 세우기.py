import sys
input=sys.stdin.readline
ans=[]
n,m=map(int,input().split())

# 간선그래프와 피간선개수 표 작성
g=[[] for _ in range(n+1)]
cnt=[0]*(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  g[a].append(b)
  cnt[b]+=1

from collections import deque
q=deque()

# 피간선개수가 0인 지점 전부 삽입
for i in range(1,n+1):
  if cnt[i]==0:
    q.append(i)

while q:
    p=q.popleft()
    ans.append(p)
    for i in g[p]:
      cnt[i]-=1
      # 피간선개수가 0이 되면 바로 삽입해주는 것이 포인트
      if cnt[i]==0:
            q.append(i)
      
print(*ans)
