def partition(a,low,high):
    key=a[low]
    i=low+1
    j=high
    while i<=j:
        while key>a[i]:
            i=i+1
        while key<a[j]:
            j=j-1
        if i<j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    
    temp=a[low]
    a[low]=a[j]
    a[j]=temp
    return j
            

def quicksort(a,low,high):
    if low<high:
        j=partition(a,low,high)
        quicksort(a,low,j-1)
        quicksort(a,j+1,high)
        

a=[0,0,0,0,0]
n=int(raw_input("enter n"))
for i in range (0,n):
    a[i]=int(raw_input(" "))
quicksort(a,0,n-1)
for i in range(0,n):
    print a[i]
