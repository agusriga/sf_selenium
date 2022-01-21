#python3 -m pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("/Users/agus/Projects/sf_selenium/googlechrome.dmg")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@title=\"Search"]").send_keys('Skillfactory')

driver.save_screenshot('sf.png')
driver.quit()