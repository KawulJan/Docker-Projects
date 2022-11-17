from time import sleep
from selenium.webdriver.common.desired_capabilites import DesiredCapabilites
from selenium import webdriver

sleep(5)

driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilites=DesiredCapabilites.CHROME)
driver.get('https://python.org')
driver.save_screenshot('screenshot.png')