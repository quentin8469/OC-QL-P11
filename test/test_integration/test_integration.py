
import pytest
#import server
import time
from selenium import webdriver

#club = server.clubs[0]['email']


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('http://127.0.0.1:5000/')
email = driver.find_element_by_name('email')
email.send_keys('john@simplylift.co')
driver.find_element_by_tag_name('button').click()
time.sleep(2)
driver.find_elements_by_id('book')[0].click()
time.sleep(2)
places = driver.find_element_by_name('places')
places.send_keys('2')
time.sleep(2)
driver.find_element_by_tag_name('button').click()
time.sleep(2)
driver.quit()
