import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
time.sleep(1)
driver.implicitly_wait(10)

#Нажмите на вкладку "My Account Menu"
driver.find_element_by_link_text('My Account').click()
time.sleep(1)

#-REGISTRATION-
##В разделе "Register", введите email для регистрации
#email_field = driver.find_element_by_id("reg_email")
#email_field.send_keys("alexis@mail.ru")
#time.sleep(3)

##В разделе "Register", введите пароль для регистрации
#password_field = driver.find_element_by_id("reg_password")
#password_field.send_keys("123Medium456Strong789")
#time.sleep(2)

##Нажмите на кнопку "Register"
#driver.find_element_by_name('register').click()
#time.sleep(2)

#-LOGIN-
#Откройте http://practice.automationtesting.in/
#Нажмите на вкладку "My Account Menu"
#В разделе "Login", введите email для логина
username_or_email_field = driver.find_element_by_id("username")
username_or_email_field.send_keys("alexis@mail.ru")
time.sleep(1)

#В разделе "Login", введите пароль для логина
password_log_field = driver.find_element_by_id("password")
password_log_field.send_keys("123Medium456Strong789")
time.sleep(1)

#Нажмите на кнопку "Login"
driver.find_element_by_name('login').click()
time.sleep(1)

element = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link"
                                            ".woocommerce-MyAccount-navigation-link--customer-logout")
element_text = element.text
assert element_text == 'Logout'

driver.quit()