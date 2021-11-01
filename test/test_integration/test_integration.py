
import pytest
#from server import clubs
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


    


#club = clubs[0]['email']


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('http://127.0.0.1:5000/')
time.sleep(2)
#email = driver.find_element_by_name('email').send_keys("john@simplylift.co")
email = driver.find_element(By.NAME, 'email').send_keys("john@simplylift.co")
driver.find_element(By.TAG_NAME,'button').click()
time.sleep(2)
#driver.find_elements_by_link_text('Book Places')[0].click()
driver.find_element(By.ID,'book').click()
#driver.find_elements_by_id('book')[0].click()
time.sleep(2)
places = driver.find_element(By.NAME,'places').send_keys('2')
#places = driver.find_element_by_name('places').send_keys('2')
time.sleep(2)
driver.find_element(By.TAG_NAME,'button').click()
time.sleep(2)
#driver.find_elements_by_id('logout')[0].click()
driver.find_elements(By.ID,'logout')[0].click()
time.sleep(2)
driver.quit()
