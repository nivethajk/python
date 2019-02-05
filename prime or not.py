a=int(input("Enter the number: "))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("The entered number is Prime Number")
else:
    print("The entered number is not a Prime Number")
