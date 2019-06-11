mydict1={"yls1":123,"yls2":456,"yls3":789}
mydict2={"yls4":123,"yls5":456,"yls6":789}
if "yls1" in mydict1:
    print("found")

mydict1.update(mydict2)
print(mydict1)
mydict={"yls1":123,"yls2":456,"yls3":789}
mydict["yls1"]=111
mydict["yls4"]=444
print(mydict.items())
del(mydict["yls1"])
print(mydict.items())
mydict.clear()
print(mydict.items())