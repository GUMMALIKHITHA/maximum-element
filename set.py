a=[1,2,1,2,1,4,5,6,7,73,23,7,8,8,2,1,3]
min=a[0]
n=len(a)
for i in range(n):
    if a[i]<min:
        min=a[i]
print(min)
