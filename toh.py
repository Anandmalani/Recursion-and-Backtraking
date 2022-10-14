def toh(n,s,h,d):
    if n==1:
        print("move disk from "+s+" to "+d)
        return
    toh(n-1,s,d,h)
    print("move disk from "+s+" to "+d)
    toh(n-1,h,s,d)

toh(3,"s","h","d")
