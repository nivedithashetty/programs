a=[]

def mergeSort(arr,low,mid,high):
    temp=[]
    l=low;
    i=low;
    m=mid+1;
    while l<=mid and m<=high:
        if(arr[l]<=arr[m]):
             temp[i]=arr[l]
             l=l+1
        else:
            temp[i]=arr[m]
            m=m+1
        i=i+1


    if l>mid:
        for k in range(m,high+1):
             temp[i]=arr[k];
             i=i+1
         
    else:
        for k in range(l,mid+1):
            temp[i]=arr[k]
            i=i+1
   
    for k in range(low,high+1):
        arr[k]=temp[k]
   
def partition(arr,low,high):
    if(low<high):
        mid=(low+high)/2
        partition(arr,low,mid)
        partition(arr,mid+1,high)
        mergeSort(arr,low,mid,high)

print "Enter the total number of elements: "
n=int(raw_input(" "))

print "Enter the elements which to be sort: "
for i in range(0,n):
    a.append(int(raw_input(" ")))
         
partition(a,0,n-1);
print("After merge sorting elements are: ");
for i in range(0,n):
    print a[i]
         


