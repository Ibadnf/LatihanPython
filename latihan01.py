mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)
print(mylist[1:])

for x in mylist:
	print(x)

mybullet=["Nol","Satu","Dua"]
for x in mybullet:
	print(x)

myint=2
myage=3
print(myint*myage)


theList=["Anna","Hana","Rama","Papa","Mama"]
print(theList[2:3])
print(theList[:3])
print(theList[-1])
for x in theList:
	if x=="Anna":
		continue
	print(x)