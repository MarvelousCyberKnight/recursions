def check(n):
    if n<2:
        return (n%2 == 0)
    else:
        return check(n-2)
n=int(input())
if (check(n)==True):
    print("Even!")
else:
    print("Odd!")
