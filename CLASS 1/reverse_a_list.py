li =[1,2,3,4,5,6]
for i in range(len(li)):
    print(li[len(li)-1-i])
    li[i]=li[len(li)-i-1]


print(li)