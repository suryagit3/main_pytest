from base_class import *
from base_class import Test_init as bc
# from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException

class Test_class_one():
    def setup_method(self,method):
        driver = init()
        self.driver = driver
    def locators(self,locator_name,locator_element,type):
        locator_dict = {"id":By.ID,"css":By.CSS_SELECTOR,"xpath":By.XPATH,"link":By.LINK_TEXT,"plink":By.PARTIAL_LINK_TEXT,
            "tagname":By.TAG_NAME,"name":By.NAME,"classname":By.CLASS_NAME}
        if locator_name in locator_dict:
            element = None
            if type == 1:
                element = self.driver.find_element(locator_dict[locator_name],locator_element)
            elif type == 2:
                element = self.driver.find_elements(locator_dict[locator_name],locator_element)
        else:
            raise KeyError
        return element
    def test_one(self):        
        # self.driver.get("https://www.google.com")
        first_ip = self.locators("csss",bc.input_field,1)
        first_ip.clear()
        first_ip.send_keys("multi inputs are sent")
        time.sleep(2)
        first_ip.clear()
        first_ip.send_keys("hih")
        time.sleep(2)
        print("method one made successfully")
    # @pytest.fixture
    def test_two(self):
        first_ip = self.locators("css",bc.input_field,1)
        first_ip.send_keys("method two")
        time.sleep(1)
        print("method two made successfully")
    def teardown_method(self,method):
        self.driver.quit()

# object_Test_class_one = Test_class_one()
# object_Test_class_one.setup_method(webdriver)
# object_Test_class_one.test_one("acd")
# object_Test_class_one.teardown_method(webdriver)