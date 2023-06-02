def fibonacci(n):
    a=0
    b=1
    sum=0
    if num<=0:
        print("Please, Enter the natural number")
    else:
        for i in range(0,num):
            print(sum)
            a=b
            b=sum
            sum=a+b
num=int(input("Enter the value of n= "))
fibonacci(num)