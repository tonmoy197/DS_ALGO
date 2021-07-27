a = [1,2,3,4,5,6]
lo=0
hi=len(a)-1
while lo<hi:
    tmp = a[lo]
    a[lo]=a[hi]
    a[hi]=tmp
    lo+=1
    hi-=1
print(a) 