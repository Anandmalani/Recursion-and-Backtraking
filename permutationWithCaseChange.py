def abc(s,arr,out):
    if len(s)==0:
        arr.append(out)
        return
    out1=(out+s[0].upper())
    out2=(out+s[0].lower())
    s=s[1:]
    abc(s,arr,out1)
    abc(s,arr,out2)
arr=[]
abc("ABC",arr,"")
print(arr)
    