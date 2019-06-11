from selenium import webdriver
#鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
#键盘事件
from selenium.webdriver.common.keys import Keys
#显示等待
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
driver.get("https://www.baidu.com")
print(driver.title)
wait.until(lambda driver:driver.find_element_by_xpath("//input[@id='kw']"))
ele1=driver.find_element_by_xpath("//input[@id='kw']")
ele1.send_keys("京东")
ele3=driver.find_element_by_xpath("//input[@id='su']").click()
wait.until(lambda driver:driver.find_element_by_xpath("//div[@id='1']/h3[@class='t']/a[1]"))
ele4=driver.find_element_by_xpath("//div[@id='1']/h3[@class='t']/a[1]").click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
"""
driver.get("https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d1875f18f9c147acafe5ea1f1023b1bb")
print(driver.title)
print(driver.current_url)
#driver.maximize_window()
wait.until(lambda driver:driver.find_element_by_xpath("//input[@id='key']"))
ele2=driver.find_element_by_xpath("//input[@id='key']")
ele2.send_keys("手机2")
time.sleep(2)
ele2.send_keys(Keys.BACK_SPACE)
ele2.send_keys(Keys.ENTER)
"""
"""
wait.until(lambda driver:driver.find_element_by_link_text("我的京东"))
ele=driver.find_element_by_link_text("我的京东")
ActionChains(driver).move_to_element(ele).perform()

wait.until(lambda driver:driver.find_element_by_link_text("待处理订单"))
ele2=driver.find_element_by_link_text("待处理订单")
ele2.click()
"""
"""
ele=driver.find_element_by_xpath("//input[@id='kw']")
print(ele.get_attribute("name"))
print(ele.tag_name) #标签名
ele.clear()
ele.send_keys("上海")
time.sleep(2)
ele.clear()
"""
"""
# 浏览器打开网址
driver.get("https://www.baidu.com")
#休眠一秒
time.sleep(1)
# 浏览器最大化
driver.maximize_window()
# 设置浏览器的高度为800像素，宽度为480像素
driver.set_window_size(480, 800)
# 浏览器后退
#driver.back()
# 浏览器前进
#driver.forward()
# 浏览器关闭
#driver.close()
# 浏览器退出
#driver.quit()
#driver.close()
#driver.quit();
"""
