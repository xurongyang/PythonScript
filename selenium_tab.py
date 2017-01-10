# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lines = open('/tmp/urls')
for line in lines:
	browser = webdriver.Chrome()
	browser.get(line)
	main_window = browser.window_handles
	while len(browser.window_handles)==1:
		time.sleep(0.1)
	browser.quit()


