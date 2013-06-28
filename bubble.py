a=[0,0,0,0,0,0]
temp=0
n=int(raw_input("enter n"))
for i in range(0,n):
    a[i]=int(raw_input(" "))
for i in range(0,n):
    for j in range(0,n-1-i):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
for i in range(0,n):
    print a[i]

    
    
