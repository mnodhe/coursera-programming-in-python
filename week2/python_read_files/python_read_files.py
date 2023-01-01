with open("example.txt",mode='r') as file:
    print("read",file.read(44))
    print("readline",file.readline())
    print("readlines",file.readlines())  