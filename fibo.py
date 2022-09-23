def fibonici(n):
    if n<=1:
        return n
    else:
        return fibonici(n-1)+fibonici(n-2)
n=int(input())
for i in range(0,n):
    print(fibonici(i),end=' ')
