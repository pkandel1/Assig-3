import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        #driver.maximize_window()
        driver.get("http://pkandel.pythonanywhere.com/home/")
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()

        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        #driver.get("http://mavsystems.pythonanywhere.com/admin/")
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[13]/a").click()
        time.sleep(1)
        driver.switch_to.alert.accept()

        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[2]/a").click()
        time.sleep(1)




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
