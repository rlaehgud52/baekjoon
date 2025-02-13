import sys
input = sys.stdin.readline
n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
li.sort(key=lambda x:x[1])
li.sort(key=lambda x:x[0])
for i in range(n):
  print(f"{li[i][0]} {li[i][1]}")