f=open("k22bs.txt","a")
#a="hii"
a=input("enter data")
f.write(a)
print("data saved in file")
f.close()


f=open("k22bs.txt","r")
#print(f.read())
d=f.read()
print(d)