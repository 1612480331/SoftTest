#coding:utf-8

import time

class Loginfo(object):
    def __init__(self):
        fname=time.strftime('%Y-%m-%d',time.gmtime())
        print(fname)
        self.log=open(fname+".txt",'w')

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()




if __name__=='__main__':
    log = Loginfo()
    log.log_write("just a test")
    log.log_close()
