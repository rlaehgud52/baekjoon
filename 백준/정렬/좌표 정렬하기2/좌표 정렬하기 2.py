import sys
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x:(x[1],x[0]))
for i in a:
  print(*i)
