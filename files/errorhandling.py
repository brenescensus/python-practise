try:
    file=open("files/example.txt","r")
    data=file.read()
    # print(data.readline())
    # print(data.readlines())
    # print(data.read())
    print(data)
except FileNotFoundError:
    print("file not found")
    
finally:
    file.close()    