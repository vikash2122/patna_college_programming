def l3(l1,l2):
    l3=[]
    for i in l1:
        print(i)
        for j in l2:
            if i==j:
                 print("found")
                 l3.append(i)
    return l3
    print(l3)   
l1=[2,3,4,5]   
l2=[3,4,5,6] 
print(l3(l1,l2))