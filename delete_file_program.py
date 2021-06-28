with open("file2.txt",'r+')as f:
    line=f.readlines()
    print(line)
    line.pop(0)
    f.writelines(line)
    print(f.readlines())