n,l=map(int,input().split())
i=1
cnt=0
while cnt<n:
    if str(l) in str(i):
        i+=1
        continue
    cnt+=1
    i+=1
print(i-1)