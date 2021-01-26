from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')

bro.get('https://qzone.qq.com')

bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id('switcher_plogin')

a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
loginBtn_tag = bro.find_element_by_id('login_button')

userName_tag.send_keys('530025909')
password_tag.send_keys('123456')
loginBtn_tag.click()
