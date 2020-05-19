#print fiboanacci series
n1=0
n2=1
n=int(input("Enter the number of term of the fibonacci series: "))
print(n1)
print(n2)
for i in range(0,n-2):
    s = n1 + n2
    print(s)
    n1 = n2
    n2 = s
