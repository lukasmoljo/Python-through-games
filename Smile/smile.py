n, m = map(int, input().split())
grid = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    tmp = input()
    for j in range(0,m,1):
        if tmp[j]=="#":
            grid[i][j]=1

eyes=-1
nose=-1 
mouth=-1
start=1

for i in range(start,n-1,1):
    s=sum(grid[i])
    if s%2==1:
        break
    elif s>0:
        index=[]
        for j in range(1,m//2+1):
            if grid[i][j]==1:
                index.extend([j, m-1-j])

        ok=1
        for j in index:
            for k in range(0,int(s/2)):
                if grid[i+k][j]==1:
                    grid[i+k][j]=0
                else:
                    ok=0

        if ok==1:
            eyes=int(s/2)
            start=i+int(s/2)+1
            break

for i in range(start,n-1):
    s=sum(grid[i])
    if s > 0:
        a=i
        j=(m-1)//2
        ok=1 

        while grid[a][j]==1 and a < n-1:
            for k in range(0,a-i+1):
                if grid[a][j+k]==1:
                    grid[a][j+k]=0
                else:
                    ok=0
            a+=1
            
        if ok==1:
            nose=a-i
            start=a+1
            break

for i in range(start, n-1, 1):
    s=sum(grid[i])
    if(s > 0):
        l=1
        r=m-2
        ok=1
        while l<=r:
            if grid[i][l]==grid[i][r]:
                grid[i][l]=0
                grid[i][r]=0
            else:
                ok=0
            l+=1
            r-=1

        if ok==1:
            mouth=s
            break

ok=1
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            ok=0

if eyes>0 and nose>0 and mouth>0 and ok==1:
    print(eyes)
    print(nose)
    print(mouth)
else:
    print(-1)
