fs=open("D:\软件测试\password.txt", "r" , encoding='utf-8')
dict={}
lines=fs.readlines()
for line in lines:
    datas=lines.strip("\n")
    if "datas" in dict:
        dict["datas"]=dict["datas"]+1
    else:
        dict["datas"]=1
for k,v in dict.items():
    print(k,v)
