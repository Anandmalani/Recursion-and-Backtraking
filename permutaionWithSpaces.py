def abc(s,arr,out):
    if len(s)==0:
        arr.append(out)
        return
    out1=out+" "+s[0]
    out2=out+s[0]
    s=s[1:]
    abc(s,arr,out1)
    abc(s,arr,out2)
    
arr=[]
abc("BC",arr,"A") 
print(arr)