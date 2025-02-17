n,m=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
ans=[]

def dfs(x):
    if x==m:
        print(*ans)
        return
    for i in li:
        if i not in ans:
            ans.append(i)
            dfs(x+1)
            ans.pop()
dfs(0)
            