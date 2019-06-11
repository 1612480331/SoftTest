#coding:utf-8


def get_userinfo(path):
    userinfoList=[]
    userconfig=open(path)


    for line in userconfig:

        accountdict = {}
        result = [ele.strip() for ele in line.split(" ")]
        for r in result:
           account= [ele.strip() for ele in r.split("=")]
           accountdict[account[0]]=account[1]
        userinfoList.append(accountdict)

    return userinfoList


if __name__=="__main__":
    #info=get_webinfo("c:\webinfo.txt")
    info=get_userinfo("userinfo.txt")
    for item in info:
        print(item)