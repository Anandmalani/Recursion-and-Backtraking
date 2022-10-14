def abc(arr,x,y):
    if len(arr)==0:
        if x in y:
        # y.append(x)
            return 
        else:
            y.append(x)
            return
    out1=x
    
    out2=[*x ,arr[0]]
    arr=arr[1:]
    abc(arr,out1,y)
    abc(arr,out2,y)
    return y

arr=[1,2,2]
x=[]
y=[]
print(abc(arr,x,y))