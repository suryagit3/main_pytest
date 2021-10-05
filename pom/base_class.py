from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Test_init():    
    input_field = "input[name='q']"
    def init_one():
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        driver.implicitly_wait(5)
        return driver
    def init():
        drv = Test_init.init_one()
        return drv
def init():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    return driver
