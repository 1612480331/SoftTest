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
def deleteAll(wait,driver):
    flag=1
    while flag==1:
        #判断是否有子板块
        try:
            xpath="//tbody[3]/tr[2]/td[5]/a/span"
            findElement(wait,driver,xpath)
            xpath="//tbody[3]/tr[1]/td[5]/a/span"
            findElement(wait,driver,xpath).click()

        except Exception as e:
            #判断是否已经删完
            try:
                xpath="//tbody[4]/tr/td[5]/a/span"
                findElement(wait,driver,xpath).click()
            except Exception as e:
                xpath = "//tbody[3]/tr[1]/td[5]/a/span"
                findElement(wait, driver, xpath).click()
                flag=0
        xpath = "//input[@value='确认删除']"
        findElement(wait, driver, xpath).click()
        xpath = "//input[@value='确定']"
        findElement(wait, driver, xpath).click()
        time.sleep(1)


if __name__ == '__main__':
    driver = openBrower()
    wait = WebDriverWait(driver, 1)
    url = "http://localhost/upload/admin.php"
    openUrl(driver, url)
    time.sleep(1)
    #登录
    logOn(wait,driver)
    #点击板块管理
    xpath="//a[@id='setforum']"
    findElement(wait,driver,xpath).click()
    #进入iframe
    driver.switch_to.frame("main")
    #删除所以板块
    deleteAll(wait,driver)

