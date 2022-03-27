import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
time.sleep(3)
driver.implicitly_wait(10)
#Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 700);")
time.sleep(1)
#Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
driver.find_element_by_css_selector('li.post-160.product.type-product.status-publish.has-post-thumbnail'
                                    '.product_cat-selenium.product_tag-ruby.product_tag-selenium.has-post-title'
                                    '.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author'
                                    '.first.outofstock.downloadable.taxable.shipping-taxable.purchasable'
                                    '.product-type-simple>a.woocommerce-LoopProduct-link>h3').click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
#Нажмите на вкладку "REVIEWS"
driver.find_element_by_css_selector('li.reviews_tab>a').click()
time.sleep(1)
#Поставьте 5 звёзд
driver.find_element_by_class_name('star-5').click()
time.sleep(1)
#Заполните поле "Review" сообщением: "Nice book!"
driver.execute_script("window.scrollBy(0, 300);")
review_field = driver.find_element_by_id("comment")
review_field.send_keys("Nice book!")
time.sleep(1)
#Заполните поле "Name"
name_field = driver.find_element_by_id("author")
name_field.send_keys("Alex")
time.sleep(1)
#Заполните "Email"
email_field = driver.find_element_by_id("email")
email_field.send_keys("alexis@mail.ru")
time.sleep(1)
#Нажмите на кнопку "SUBMIT"
driver.find_element_by_name('submit').click()
time.sleep(2)
driver.quit()