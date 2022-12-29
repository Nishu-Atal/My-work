x=int(input("Enter a number-"))
for i in range(2,x,1):
    if x % i==0:
        print("Given number is not a prime number")
        break
else:
    print("Given number is prime number")