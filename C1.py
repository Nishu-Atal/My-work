a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if a>b:
    if c>a:
        print("Greater number is-",c)
    else:
        print("Greater number is-",a)
else:
    if b>c:
        print("Greater number is-", b)
    else:
        print("Greater number is-", c)
