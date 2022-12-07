# question 3

s=int(input("enter the speed: "))
def limit(s):
    if s<70:
        print('Ok')
    else:
        d=s-70
        k=d//5
        if k<=12:
            print("Points:",k)
        else:
            print("License suspended")
limit(s)
