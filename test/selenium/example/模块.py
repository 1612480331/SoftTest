from selenium import webdriver
#鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
#键盘事件
from selenium.webdriver.common.keys import Keys
#显示等待
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlrd
import sys

def openExcel(filePath):
    try:
        data = xlrd.open_workbook(filePath)
    except Exception as e:
        print(str(e))
    table = data.sheets()[0]
    rows = table.nrows
    cols = table.ncols
    colNames = table.row_values(0)
    print(len(colNames))
    list = []
    for row in range(1, rows):
        rowValue = table.row_values(row)
        if rowValue:
            dict = {}
            for i in range(cols):
                dict[colNames[i]] = rowValue[i]
            list.append(dict)
    return list

def openBrower():
    return webdriver.Chrome()
def openUrl(driver,url):
    driver.get(url)
    driver.maximize_window()
def findElement(wait,driver,xpath):
    wait.until(lambda driver: driver.find_element_by_xpath(xpath))
    ele = driver.find_element_by_xpath(xpath)
    return ele

#发表一个论坛流程
def publishProcess(wait,driver,item):
    # 发表
    xpath = "//img[@id='td_post']"
    ele3 = findElement(wait, driver, xpath)
    ActionChains(driver).move_to_element(ele3).perform()
    time.sleep(1)
    # 新帖
    xpath = "//div[@id='pw_box']/div[@class='menu-b']/a[1]"
    ele2 = findElement(wait, driver, xpath)
    ele2.click()
    add(wait, driver, item)
#输入论坛标题和内容
def add(wait,driver,item):
    # 标题输入框
    xpath = "//input[@id='atc_title']"
    ele1 = findElement(wait, driver, xpath)
    ele1.clear()
    ele1.send_keys(item['title'])
    time.sleep(1)
    # 文章内容输入区域
    xpath = "//textarea[@id='textarea']"
    ele1 = findElement(wait, driver, xpath)
    ele1.clear()
    ele1.send_keys(item['content'])
    time.sleep(1)
    # 提交按钮
    xpath = "//input[@class='btn']"
    ele1 = findElement(wait, driver, xpath).click()
def logOn(wait,driver):
    # 登录链接
    xpath = "//a[@class='ml b']"
    ele1 = findElement(wait, driver, xpath).click()
    # 用户名
    xpath = "//input[@name='pwuser']"
    ele1 = findElement(wait, driver, xpath)
    ele1.clear()
    ele1.send_keys("admin")
    time.sleep(1)
    # 密码
    xpath = "//input[@name='pwpwd']"
    ele1 = findElement(wait, driver, xpath)
    ele1.clear()
    ele1.send_keys("admin")
    time.sleep(1)
    # 登录按钮
    xpath = "//input[@class='btn']"
    ele1 = findElement(wait, driver, xpath).click()
class Loginfo(object):
    def __init__(self):
        fname=time.strftime('%Y-%m-%d',time.gmtime())
        self.log=open(sys.path[0]+fname+".txt",'w',encoding='utf-8')
    def writeSuccess(self,item):
        self.log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+
                       ":  "+"title:"+item['title']+"  content:"+item['content']+"  Pass"+"\n")
    def writeError(self,item,msg):
        self.log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
                       ":  "+"title:"+item['title']+"  content:"+item['content'] +"  error:" +msg+"\n")
    def log_close(self):
        self.log.close()


if __name__ == '__main__':
    log=Loginfo()
    driver = openBrower()
    wait = WebDriverWait(driver, 10)
    url = "http://localhost/upload/index.php"
    openUrl(driver, url)
    time.sleep(1)

    #默认模块
    xpath="//a[@id='fn_2']"
    ele1=findElement(wait,driver,xpath)
    time.sleep(1)
    ele1.click()
    logOn(wait,driver)
    time.sleep(1)
    # 获取excel表中的数据
    filePath = "D:\软件测试\功能测试\帖子.xlsx"
    list = openExcel(filePath)
    #print(list)
    flag=1
    for item in list:
        if not isinstance(item['title'],str):
            item['title']=str(item['title']).strip()
        if not isinstance(item['content'],str):
            item['content'] = str(item['content']).strip()
        if flag==1:
            publishProcess(wait, driver,item)
        else:
            add(wait, driver, item)
        try:
            xpath = "//input[@class='bt' and @style]"
            findElement(wait,driver,xpath)
            """
            wait.until(lambda driver: driver.find_element_by_xpath(xpath))
            ele = driver.find_element_by_xpath(xpath)
            """
            flag = 0
            # alert=driver.switch_to.alert()
            xpath = "//p"
            ele = findElement(wait, driver, xpath)
            ele1 = findElement(wait, driver, xpath)
            error = ele1.text
            log.writeError(item, error)
            xpath = "//input[@class='bt' and @style]"
            ele.click

        except Exception as e:
            flag = 1
            log.writeSuccess(item)
        """
        if item['title'].strip() and len(item['title']) <100 and len(item['content']) >3 and len(item['content']) <50000:
            flag=1
            log.writeSuccess(item)
        else:
            flag=0
            # alert=driver.switch_to.alert()
            xpath = "//p"
            ele = findElement(wait, driver, xpath)
            ele1 = findElement(wait, driver, xpath)
            error = ele1.text
            log.writeError(item,error)
            xpath = "//input[@class='bt' and @style]"
            ele.click
        """
    log.log_close()
