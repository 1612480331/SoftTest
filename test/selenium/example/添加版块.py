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

def openBrower():
    return webdriver.Chrome()
def openUrl(driver,url):
    driver.get(url)
    driver.maximize_window()
def findElement(wait,driver,xpath):
    wait.until(lambda driver: driver.find_element_by_xpath(xpath))
    ele = driver.find_element_by_xpath(xpath)
    return ele

def input(wait,driver,xpath,text):
    ele = findElement(wait, driver, xpath)
    ele.clear()
    ele.send_keys(text)
    time.sleep(1)
def logOn(wait,driver):
    xpath = "//input[@class='input pw2']"
    input(wait, driver, xpath, "admin")
    xpath = "//input[@class='input pwpd2']"
    input(wait, driver, xpath, "admin")
    xpath = "//input[@name='submit']"
    findElement(wait, driver, xpath).click()
def createClass(wait,driver,className):
    # 类输入框
    xpath = "//input[@name='name']"
    input(wait, driver, xpath, className)
    # 提交
    xpath = "//input[@class='btn']"
    findElement(wait, driver, xpath).click()
def addBlock(wait,driver,v):
    for i in v:
        # 添加板块
        try:
            xpath = "//table/tbody[1]/tr[" + str(v.index(i) + 2) + "]/td[1]/input"
            input(wait, driver, xpath, i['order'])
            xpath = "//table/tbody[1]/tr[" + str(v.index(i) + 2) + "]/td[2]/input"
            input(wait, driver, xpath, i['name'])
        except Exception as e:
            xpath = "//span[@title='添加更多']"
            findElement(wait, driver, xpath).click()
            xpath = "//*[@id='fbody']/tr[" + str(v.index(i) - 4) + "]/td[1]/input"
            print(v.index(i) - 3)
            input(wait, driver, xpath, i['order'])
            xpath = "//*[ @ id = 'fbody']/tr[" + str(v.index(i) - 4) + "]/td[2]/input"
            input(wait, driver, xpath, i['name'])
    xpath = "//center/input[@type='submit']"
    findElement(wait, driver, xpath).click()
    xpath = "//input[@value='确定']"
    findElement(wait, driver, xpath).click()
def openExcel(filePath):
    try:
        data = xlrd.open_workbook(filePath)
    except Exception as e:
        print(str(e))
    sheetNum = data.nsheets
    list1 = []
    for i in range(sheetNum):
        dict1 = {}
        sheetName = data.sheet_names()[i]
        table = data.sheets()[i]
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
        dict1[sheetName] = list
        list1.append(dict1)
    return list1
if __name__ == '__main__':
    driver = openBrower()
    wait = WebDriverWait(driver, 3)
    url = "http://localhost/upload/admin.php"
    openUrl(driver, url)
    time.sleep(1)
    #获取数据
    filePath = "D:\软件测试\功能测试\类和板块.xlsx"
    list = openExcel(filePath)
    #登录
    logOn(wait,driver)
    #点击板块管理
    xpath="//a[@id='setforum']"
    findElement(wait,driver,xpath).click()
    driver.switch_to.frame("main")
    for item in list:
        for k,v in item.items():
            # print(k,v)
            #创建一个类
            createClass(wait,driver,k)
            #添加类中板块
            addBlock(wait,driver,v)









