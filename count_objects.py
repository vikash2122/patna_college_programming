class Person:
    count=0
    def __init__(self) -> None:
        Person.count+=1
        print("this is init method")
p=Person()
p1=Person()
print(Person.count) 