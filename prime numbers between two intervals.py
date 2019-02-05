lower_limit = int(input("Enter the first number: "))
upper_limit = int(input("Enter the second number: "))
for num in range(lower_limit,upper_limit + 1):
 
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
