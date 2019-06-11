import csv
fs=open("D:\软件测试\password.txt", "r" , encoding='utf-8')
dict={}
lines=fs.readlines()
for line in lines:
    datas=line.strip("\n")
    if datas in dict:
        dict[datas]=dict[datas]+1
    else:
        dict[datas]=1
a=sorted(dict.items(),key = lambda x:x[1],reverse = True)
with open('D:\软件测试\password3.csv', 'w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in a:
       writer.writerow([key, value])
fs.close()

"""
with open('D:\软件测试\password2.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in a]
fs.close()
"""
"""
for k,v in a:
    print(k,v)
"""