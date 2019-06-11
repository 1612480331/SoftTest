mydict={"yls1":123,"yls2":456,"yls3":789}
print(mydict.items())
#方式一
for k,v in mydict.items():
    print(k,v)
#方式二
for k in mydict.keys():
    print(k,mydict[k])