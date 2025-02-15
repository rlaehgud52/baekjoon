import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
  n,k=map(int,input().split())
  time=list(map(int,input().split()))
  dp=[0]*(n+1)
  g=[[] for _ in range(n+1)]
  cnt=[0]*(n+1)
  for _ in range(k):
    a,b=map(int,input().split())
    g[a].append(b)
    cnt[b]+=1
  
  from collections import deque
  q=deque()
  for i in range(1,n+1):
    if cnt[i]==0:
      q.append(i)
      dp[i]=time[i-1]
  while q:
    p=q.popleft()
    for i in g[p]:
      cnt[i]-=1
      if dp[i]<dp[p]+time[i-1]:
        dp[i]=dp[p]+time[i-1]
      if cnt[i]==0:
        q.append(i)
  ans=int(input())
  print(dp[ans])