def abc(n,k):
    if n==1 and k==1:
        return 0
    mid=(2**(n-1))//2
    if k<=mid:
        return abc(n-1,k)
    else:
        if (abc(n-1,k-mid))==0:
            return 1
        else:
            return 0

print(abc(4,6))
    