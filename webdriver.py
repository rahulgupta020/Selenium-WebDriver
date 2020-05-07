from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager("81.0.4044.138").install())
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome(executable_path='C:/Users\rahul/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe')

import time

driver.get("https://google.com")
time.sleep(100)
driver.close()
driver.quit()