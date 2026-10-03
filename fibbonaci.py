num=int(input("Enter the number of terms:"))
fib1=0
fib2=1
for i in range(num):
    print(fib1,end="  ")
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
    

    