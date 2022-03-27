#-----------------------------------------------------------------------------------------------------------------------
##--ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА--
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
time.sleep(1)
## Реализация неявного ожидание поиска элементов
driver.implicitly_wait(10)
##Залогиньтесь
driver.find_element_by_link_text('My Account').click()
time.sleep(1)
username_or_email_field = driver.find_element_by_id("username")
username_or_email_field.send_keys("alexis@mail.ru")
time.sleep(1)
password_log_field = driver.find_element_by_id("password")
password_log_field.send_keys("123Medium456Strong789")
time.sleep(1)
driver.find_element_by_name('login').click()
time.sleep(1)
##Нажмите на вкладку "Shop"
driver.find_element_by_link_text('Shop').click()
time.sleep(1)
##Откройте книгу "HTML 5 Forms"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
driver.find_element_by_xpath("//h3[contains(text(),'HTML5 Forms')]").click()
time.sleep(3)
##Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
element = driver.find_element_by_class_name("product_title.entry-title")
element_get_text = element.text
assert element_get_text == 'HTML5 Forms'
driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
##--КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ--
#import time
#from selenium import webdriver

#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.get("http://practice.automationtesting.in/")
#driver.maximize_window()
#time.sleep(1)
## Реализация неявного ожидание поиска элементов
#driver.implicitly_wait(10)
##Логин
#driver.find_element_by_link_text('My Account').click()
#time.sleep(1)
#username_or_email_field = driver.find_element_by_id("username")
#username_or_email_field.send_keys("alexis@mail.ru")
#time.sleep(1)
#password_log_field = driver.find_element_by_id("password")
#password_log_field.send_keys("123Medium456Strong789")
#time.sleep(1)
#driver.find_element_by_name('login').click()
#time.sleep(1)
##Нажатие на вкладку "Shop"
#driver.find_element_by_link_text('Shop').click()
#time.sleep(1)

##Откройте категорию "HTML"
#driver.find_element_by_xpath("//a[contains(text(),'HTML')]").click()
#time.sleep(1)
##Добавьте тест, что отображается три товара
#items_count = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
#if len(items_count) == 3:
#    print('На странице 3 товара')
#else:
#    print('Ошибка. Количество товаров в корзине: ' + str(len(items_count)))
#driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
##--СОРТИРОВКА ТОВАРОВ--
#import time
#from selenium import webdriver
#from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.get("http://practice.automationtesting.in/")
#driver.maximize_window()
#time.sleep(1)
## Реализация неявного ожидание поиска элементов
#driver.implicitly_wait(10)
##Логин
#driver.find_element_by_link_text('My Account').click()
#time.sleep(1)
#username_or_email_field = driver.find_element_by_id("username")
#username_or_email_field.send_keys("alexis@mail.ru")
#time.sleep(1)
#password_log_field = driver.find_element_by_id("password")
#password_log_field.send_keys("123Medium456Strong789")
#time.sleep(1)
#driver.find_element_by_name('login').click()
#time.sleep(1)
##Нажатие на вкладку "Shop"
#driver.find_element_by_link_text('Shop').click()
#time.sleep(1)

##Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
#element = driver.find_element_by_name("orderby")
#element_selected = element.get_attribute("value")
#if element_selected is not None:
#    print('В селекторе выбран вариант Default sorting')
#else:
#    print('В селекторе не выбран вариант Default sorting')
##Отсортируйте товары по цене от большей к меньшей
#element = driver.find_element_by_name("orderby")
#select = Select(element)
#select.select_by_value("price-desc")
#time.sleep(1)
#driver.execute_script("window.scrollBy(0, 450);")
#time.sleep(3)
##Снова объявите переменную с локатором основного селектора сортировки
#element = driver.find_element_by_name("orderby")
##Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
#element_selected = element.get_attribute("value")
#if element_selected is not None:
#    print('В селекторе выбрана сортировка Sort by price: high to low')
#else:
#    print('В селекторе не выбрана сортировка Sort by price: high to low')
#driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
##--ОТОБРАЖЕНИЕ, СКИДКА ТОВАРА--
#import time
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.get("http://practice.automationtesting.in/")
#driver.maximize_window()
#time.sleep(1)
## Реализация неявного ожидание поиска элементов
#driver.implicitly_wait(10)
##Логин
#driver.find_element_by_link_text('My Account').click()
#time.sleep(1)
#username_or_email_field = driver.find_element_by_id("username")
#username_or_email_field.send_keys("alexis@mail.ru")
#time.sleep(1)
#password_log_field = driver.find_element_by_id("password")
#password_log_field.send_keys("123Medium456Strong789")
#time.sleep(1)
#driver.find_element_by_name('login').click()
#time.sleep(1)
##Нажатие на вкладку "Shop"
#driver.find_element_by_link_text('Shop').click()
#time.sleep(1)

##Откройте книгу "Android Quick Start Guide"
#driver.execute_script("window.scrollBy(0, 600);")
#time.sleep(1)
#driver.find_element_by_xpath("//h3[contains(text(),'Android Quick Start Guide')]").click()
#time.sleep(3)
##Добавьте тест, что содержимое старой цены = "₹600.00"
#element=driver.find_element_by_xpath("//span[contains(text(),'600.00')]")
#element_get_text = element.text
#assert element_get_text == "₹600.00"
##Добавьте тест, что содержимое новой цены = "₹450.00"
#element2=driver.find_element_by_xpath("//span[contains(text(),'450.00')]")
#element2_get_text = element2.text
#assert element2_get_text == "₹450.00"

##Добавьте явное ожидание и нажмите на обложку книги
#cover = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "attachment-shop_single.size-shop_single.wp-post-image")))
#driver.find_element_by_class_name("attachment-shop_single.size-shop_single.wp-post-image").click()
#time.sleep(3)
##Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
#close_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
#driver.find_element_by_class_name("pp_close").click()
#time.sleep(3)
#driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
#--ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ--
#import time
#from selenium import webdriver

#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.get("http://practice.automationtesting.in/")
#driver.maximize_window()
#time.sleep(1)
## Реализация неявного ожидание поиска элементов
#driver.implicitly_wait(10)
##Логин
#driver.find_element_by_link_text('My Account').click()
#time.sleep(1)
#username_or_email_field = driver.find_element_by_id("username")
#username_or_email_field.send_keys("alexis@mail.ru")
#time.sleep(1)
#password_log_field = driver.find_element_by_id("password")
#password_log_field.send_keys("123Medium456Strong789")
#time.sleep(1)
#driver.find_element_by_name('login').click()
#time.sleep(1)
##Нажатие на вкладку "Shop"
#driver.find_element_by_link_text('Shop').click()
#time.sleep(1)

##Добавьте в корзину книгу "HTML5 WebApp Development"
#driver.execute_script("window.scrollBy(0, 600);")
#time.sleep(3)
#driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']").click()
#time.sleep(3)
##Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
#element3=driver.find_element_by_css_selector("span.cartcontents")
#element3_get_text = element3.text
#assert  element3_get_text == "1 Item"
#element4=driver.find_element_by_xpath("//span[contains(text(),'₹180.00')]")
#element4_get_text = element4.text
#assert element4_get_text == "₹180.00"
##Перейдите в корзину
#driver.find_element_by_class_name("wpmenucart-contents").click()
#time.sleep(3)
##Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
#element5=driver.find_element_by_xpath("//span[contains(text(),'180.00')]")
#element5_get_text = element5.text
#assert element5_get_text == "₹180.00"
##Используя явное ожидание, проверьте что в Total отобразилась стоимость
#element6=driver.find_element_by_xpath("//span[contains(text(),'189.00')]")
#element6_get_text = element6.text
#assert element6_get_text == "₹189.00"
#driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
#--РАБОТА В КОРЗИНЕ--
#import time
#from selenium import webdriver

#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.get("http://practice.automationtesting.in/")
#driver.maximize_window()
#time.sleep(1)
## Реализация неявного ожидание поиска элементов
#driver.implicitly_wait(10)
##Логин
#driver.find_element_by_link_text('My Account').click()
#time.sleep(1)
#username_or_email_field = driver.find_element_by_id("username")
#username_or_email_field.send_keys("alexis@mail.ru")
#time.sleep(1)
#password_log_field = driver.find_element_by_id("password")
#password_log_field.send_keys("123Medium456Strong789")
#time.sleep(1)
#driver.find_element_by_name('login').click()
#time.sleep(1)
##Нажатие на вкладку "Shop"
#driver.find_element_by_link_text('Shop').click()
#time.sleep(1)

##Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
#driver.execute_script("window.scrollBy(0, 600);")
#time.sleep(1)
#driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']").click()
#time.sleep(1)
#driver.execute_script("window.scrollBy(0, 400);")
#time.sleep(1)
#driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=180']").click()
#time.sleep(1)
##Перейдите в корзину
#driver.find_element_by_class_name("wpmenucart-contents").click()
#time.sleep(3)
##Удалите первую книгу
#driver.find_element_by_xpath("//a[@data-product_id='182']").click()
#time.sleep(1)
##Нажмите на Undo (отмена удаления)
#driver.find_element_by_xpath("//a[contains(text(),'Undo?')]").click()
#time.sleep(1)
##В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
#driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]").clear()
#qty_field = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
#qty_field.send_keys("3")
#time.sleep(1)
##Нажмите на кнопку "UPDATE BASKET"
#driver.find_element_by_name("update_cart").click()
#time.sleep(3)
##Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
#element = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
#element_check = element.get_attribute("value")
#assert element_check == "3"
##Нажмите на кнопку "APPLY COUPON"
#driver.find_element_by_name("apply_coupon").click()
#time.sleep(3)
##Добавьте тест, что возникло сообщение: "Please enter a coupon code."
#element8=driver.find_element_by_xpath("//li[contains(text(),'Please enter a coupon code.')]")
#element8_get_text = element8.text
#assert element8_get_text == "Please enter a coupon code."
#driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
##--ПОКУПКА ТОВАРА--
#import time
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.get("http://practice.automationtesting.in/")
#driver.maximize_window()
#time.sleep(1)
## Реализация неявного ожидание поиска элементов
#driver.implicitly_wait(10)
##Логин
#driver.find_element_by_link_text('My Account').click()
#time.sleep(1)
#username_or_email_field = driver.find_element_by_id("username")
#username_or_email_field.send_keys("alexis@mail.ru")
#time.sleep(1)
#password_log_field = driver.find_element_by_id("password")
#password_log_field.send_keys("123Medium456Strong789")
#time.sleep(1)
#driver.find_element_by_name('login').click()
#time.sleep(1)
##Нажатие на вкладку "Shop"
#driver.find_element_by_link_text('Shop').click()
#time.sleep(1)
##Проскролльте на 300 пикселей вниз
#driver.execute_script("window.scrollBy(0, 500);")
#time.sleep(1)

##Добавьте в корзину книгу "HTML5 WebApp Development"
#driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']").click()
#time.sleep(1)
##Перейдите в корзину
#driver.find_element_by_class_name("wpmenucart-contents").click()
#time.sleep(1)
##Нажмите "PROCEED TO CHECKOUT" (Перед нажатием, добавьте явное ожидание)
#cover = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CLASS_NAME,"checkout-button.button.alt.wc-forward")))
#driver.find_element_by_class_name('checkout-button.button.alt.wc-forward').click()
#time.sleep(1)
##Заполните все обязательные поля
#first_name = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
#first_name_field = driver.find_element_by_id('billing_first_name')
#first_name_field.send_keys("Alex")
#last_name_field = driver.find_element_by_id('billing_last_name')
#last_name_field.send_keys("Grid")
#driver.find_element_by_id("billing_email").clear()
#billing_email_field = driver.find_element_by_name("billing_email")
#billing_email_field.send_keys("alexis@mail.ru")
#time.sleep(1)
#phone_field = driver.find_element_by_id('billing_phone')
#phone_field.send_keys("9567453456")
#time.sleep(1)
#driver.find_element_by_id("select2-chosen-1").click()
#country_field = driver.find_element_by_id("s2id_autogen1_search")
#country_field.send_keys("Qatar")
#driver.find_element_by_class_name("select2-match").click()
#address_field = driver.find_element_by_id('billing_address_1')
#address_field.send_keys("Blumen strasse 9")
#city_field = driver.find_element_by_id('billing_city')
#city_field.send_keys("Ashkhabad")
#state_field = driver.find_element_by_id('billing_state')
#state_field.send_keys("Rancho")
#postcode_field = driver.find_element_by_id('billing_postcode')
#postcode_field.send_keys("456")
#time.sleep(1)
##Выберите способ оплаты "Check Payments" (Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep)
#driver.execute_script("window.scrollBy(0, 600);")
#time.sleep(1)
#driver.find_element_by_id("payment_method_cheque").click()
#driver.find_element_by_id("place_order").click()
#time.sleep(1)
#text_1 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
#    (By.XPATH, "//p[@class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received."))
#text_2 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
#    (By.XPATH, "//td[contains(text(),'Check Payments')]"), "Check Payments"))
#driver.quit()