def heapify(a,n):
    for k in range(1,n):
        item=a[k]
        i=k
        j=i-1
        while item>a[j] and i>0:
            a[i]=a[j]
            i=j
            j=(i-1)/2
        a[i]=item

def adjust(a,n):
    j=0
    item=a[j]
    i=2*j+1
    while i<n-1:
        if i+1<n-1:
            if a[i]<a[i+1]:
                i=i+1
        if item<a[i]:
            a[j]=a[i]
            j=i
            i=2*j+1
        else:
            break
    a[j]=item

def heapsort(a,n):
    heapify(a,n)
    for i in range(n-1,0,-1):
        temp=a[i]
        a[i]=a[0]
        a[0]=temp
        adjust(a,i)

a=[]
n=int(raw_input("enter n"))
for i in range(0,n):
    a.append(int(raw_input(" ")))
heapsort(a,n)
for i in range(0,n):
    print a[i]
  
