a=()
x=input("enter the value of a")
print(x)
a=x.split(' ')
print(a)
a=[int(i) for i in a] #a=list(map(int,a))
for j in range(len(a)-1):
    for i in range(0,len(a)-1-j):
        if a[i]>a[i+1]:
            print(a[i],a[i+1])
            a[i],a[i+1]=a[i+1],a[i]
print(a)