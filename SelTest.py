from selenium import webdriver
browser = webdriver.Chrome('chromedriver')
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
button= browser.find_element_by_class_name('btn-default')
user_messag= browser.find_element_by_id('user-message')
# user_messag.clear()
user_messag.send_keys("I Am an Expert")
button.click()