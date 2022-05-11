from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://karnatakalms.com/home")

input=driver.find_element_by_xpath('//*[@id="homebody"]/div[2]/div/button[2]').click()

input=driver.find_element_by_xpath('//*[@id="userid"]')
input.send_keys('ug19snnajaja')

input=driver.find_element_by_xpath('//*[@id="password"]')
input.send_keys('11082000')

input=driver.find_element_by_xpath('/html/body/app-root/app-layout-full/div[1]/main/div/app-login/div/div/div/div[2]/div/div[1]/form/div[3]/select').click()

#currently working on drop handling button so plz select required university and leave it 
time.sleep(6)

input=driver.find_element_by_xpath('/html/body/app-root/app-layout-full/div[1]/main/div/app-login/div/div/div/div[2]/div/div[1]/form/div[4]/div/button').click()



