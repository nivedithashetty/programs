a=[]
n=int(raw_input("enter n"))
for i in range(0,n):
      a.append(int(raw_input(" ")))
      
for i in range(1,n):
      j=i-1
      temp=a[i]
      while a[j]>temp:
          a[j+1]=a[j]
          j=j-1
      a[j+1]=temp
      
     

      
for i in range(0,n):
      print a[i]
