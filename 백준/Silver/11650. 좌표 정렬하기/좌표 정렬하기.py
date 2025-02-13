import sys
input = sys.stdin.readline
n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
li.sort()
for i in li:
  print(i[0],i[1])