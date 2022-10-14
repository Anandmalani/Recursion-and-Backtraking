def abc(n,o,c,out):
    if c==0:
        print(out)
        return
    if o==0:
        out=out+")"
        c=c-1
        abc(n,o,c,out)
    elif o==c:
        out=out+"("
        
        abc(n,o-1,c,out)
    else:
        out1=out+"("
        out2=out+")"
        abc(n,o-1,c,out1)
        abc(n,o,c-1,out2)


abc(3,3,3,"")