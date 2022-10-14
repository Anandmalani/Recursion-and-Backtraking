


def abc(inp, out):
    if len(inp)==0:
        print(out)
        return
    
    out1=out
    out2=out+inp[0]
    inp=inp[1: ]
    abc(inp,out1)
    abc(inp,out2)

abc("abc","")

x="a"
x=x[1:]
print(x)