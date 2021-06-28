c=open("file_handling.txt",'r')
line=(c.read())
f=open('copy_file_handling.txt','w')
f.write(line)
print(line)
c.close()
f.close()
f=open('copy_file_handling.txt','r')
print(f.read())
f.close()


