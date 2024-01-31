def check(n1):
    match n1:
        case 2:
            print("mathced with 2")
        case 3:
            print("mathced with 3")
        case 5:
            print("mathced with 5")
        case 7:
            print("mathced with 7")     
        case 11:
            print("mathced with 11")
        case _ :
            print("not matched in these small prime numbers")


c= int(input("enter any number: "))
check(c)


def find(a):
    for i in arr:
        if i % 2==0:
            print("the even numbers are",i)
        else:
            print("the odd numbers are", i)



arr =[1,2,3,4,5,6,7]

find(arr)


