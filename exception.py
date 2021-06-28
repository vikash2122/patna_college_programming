class Myexcept(Exception):
    print("zero division error")
class Zero_division():
    try:
        x=int(input("enter 1st a number:"))
        y=int(input("enter 2nd a number:"))
        z=x/y
        raise Myexcept
    except(ZeroDivisionError):
        print("value error")
        
