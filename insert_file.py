def insert(myfile1,pos,lnnum,Istring): 
    c1=open(myfile1,"r+")
    c1.seek(pos,lnnum)
    tail=c1.read()
    c1.seek(pos,lnnum)
    c1.write(Istring)
    c1.write(tail)
    c1.close()

