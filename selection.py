a=[0,0,0,0,0,0,0,0,0,0]
temp=0
pos=0
n=int(raw_input("enter n"))
for i in range (0,n):
    a[i]=int(raw_input(" "))
for i in range(0,n-1):
    pos=i
    for j in range(i+1,n):
        if a[j]<a[pos]:
            pos=j
    temp=a[pos]
    a[pos]=a[i]
    a[i]=temp

print"sorted array is "
for i in range(0,n):
    print a[i]
