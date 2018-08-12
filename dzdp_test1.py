from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://account.dianping.com")

time.sleep(1)
frame_xpath = driver.find_element(By.XPATH, '//*[@id="J_login_container"]/div/iframe')
driver.switch_to.frame(frame_xpath)

time.sleep(1)
driver.implicitly_wait(20)
el = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/span')
el.click()

driver.implicitly_wait(20)
el = driver.find_element(By.ID, 'mobile-number-textbox')
#el.send_keys('17782629431')
el.send_keys('15609100803')

driver.implicitly_wait(20)
el = driver.find_element(By.ID, 'send-number-button')
el.click()

verification_code = input("请输入手机上的动态验证码：")
verification_code = str(verification_code)

driver.implicitly_wait(20)
el = driver.find_element(By.ID, 'number-textbox')
el.send_keys(verification_code)

driver.implicitly_wait(20)
el = driver.find_element(By.ID, 'login-button-mobile')
el.click()

#霸王餐
driver.implicitly_wait(20)
el = driver.find_element(By.XPATH, '//*[@id="header-container"]/div[3]/div[1]/div/a[2]')
el.click()

#切换到霸王餐页面
time.sleep(1)
all_hand = driver.window_handles
print(all_hand)
driver.switch_to.window(all_hand[-1])

#美食
time.sleep(1)
driver.implicitly_wait(20)
el_num = driver.find_element(By.XPATH, '//*[@id="s-fix"]/div[2]/div[1]/div[2]/span')
el_num.click()

#电子券
driver.implicitly_wait(20)
el = driver.find_element(By.XPATH, '//*[@id="filter-types"]/div[3]')
el.click()

#加载更多
driver.implicitly_wait(20)
el = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/a')
el.click()

#获得循环总数--美食数量
time.sleep(1)
patten = re.compile(r'\d+')
result = patten.findall(el_num.text)
print(el_num.text)
print(result)
result = int(result[0])
print(result)

#循环阶段
#具体图片链接-li元素自增
for i in range(1, result):

    time.sleep(1)
    driver.implicitly_wait(20)
    locator = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[%s]/a/div[1]/img' %i)
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))

    el = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[%s]/a/div[1]/img' %i)
    print('/html/body/div[2]/div[2]/div[2]/div[2]/ul/li[%s]/a/div[1]/img' %i)
    el.click()
    print('正在点击第%s个图片' %i)

    #切换到具体美食页面
    time.sleep(1)
    all_hand = driver.window_handles
    print(all_hand)
    driver.switch_to.window(all_hand[-1])

    #判断【我要报名】还是【修改报名】
    time.sleep(1)
    driver.implicitly_wait(20)
    locator = (By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/span/a')
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))

    el = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[2]/span/a')
    isSign = el.text
    if '我要报名' in isSign:
        driver.implicitly_wait(20)
        el.click()

        #确认
        time.sleep(1)
        driver.implicitly_wait(20)
        locator = (By.ID, 'J_pop_ok')
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))

        el = driver.find_element(By.ID, 'J_pop_ok')
        el.click()

        #点击关闭
        time.sleep(1)
        driver.implicitly_wait(20)
        el = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[1]/a')
        el.click()

        #关闭当前tab页面
        time.sleep(1)
        driver.close()

        time.sleep(1)
        all_hand = driver.window_handles
        print(all_hand)
        driver.switch_to.window(all_hand[-1])

    else:
        time.sleep(1)
        driver.close()
        time.sleep(1)
        all_hand = driver.window_handles
        print(all_hand)
        driver.switch_to.window(all_hand[-1])




time.sleep(10)