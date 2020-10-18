from selenium import webdriver
import time

driver = webdriver.Safari()

driver.get("https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession")

username = driver.find_element_by_xpath('//*[@id="identifierId"]')
username.click()
username.send_keys('2019dhruvisha.mondhe@ves.ac.in')

next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next.click()

time.sleep(10)

password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('Dhruvisha_2001')

next = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()

time.sleep(15)
classroom = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]')
classroom.click()

time.sleep(20)
link = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div')
link.click()

print(driver.title)
to_switch_tab = driver.window_handles[1]
driver.switch_to_window(to_switch_tab)
print(driver.title)


time.sleep(35)

#Turns off mic and camera and joins the meet
camera = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[3]/div[2]/div/div')
camera.click()

#mic = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[1]/div/div[3]/div[1]/div/div/div')
#mic.click()

#join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
#join.click()
