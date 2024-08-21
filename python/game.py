def gamefunc(arr):
    arr2=[]
    for i in arr:
        if i=="D":
            arr2.append(2*(arr2[len(arr2)-1]))
        elif i=="C" :
            arr2.pop()
        elif i=="+":
            arr2.append(arr2[len(arr2)-1]+arr2[len(arr2)-2])
        else:
            arr2.append(int(i))
    total=sum(arr2)
    print (total)

arr3=["5", "2", "C", "D", "+"]
gamefunc(arr3)    