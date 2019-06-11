mylist=[1,2,3,4,5,6]
"""
for item in mylist:
    if item==3:
        item=100
print(mylist)
"""
for i in mylist:
    print(mylist.index(i))

for i in range(len(mylist)):
    if mylist[i]==3:
        mylist[i]=10
print(mylist)