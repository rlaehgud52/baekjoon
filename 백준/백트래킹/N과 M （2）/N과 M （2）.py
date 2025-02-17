n,m=map(int,input().split())
ans=[]

#dfs의 인수는 다양하게 들어올 수 있음
def dfs(x,last):
    
    #백트래킹의 첫번째에서는 if terminal을 먼저 적어준다
    if x==m:
        print(*ans)
        return
    #완전 탐색 반복문과 재귀 dfs를 적어준다
    for i in range(last+1,n+1):
        ans.append(i)
        dfs(x+1,i)
        ans.pop()

dfs(0,0)
