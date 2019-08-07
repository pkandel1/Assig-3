import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "3900team1"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://3900team1.pythonanywhere.com//admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://3900team1.pythonanywhere.com/admin")
       assert "Logged In"
       time.sleep(1)


       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_code")
       elem.send_keys("team1a")
       elem = driver.find_element_by_id("id_valid_from_0")
       elem.send_keys("2019-08-02")
       time.sleep(2)

       elem = driver.find_element_by_id("id_valid_from_1")
       elem.send_keys("06:00:00")
       time.sleep(2)

       elem = driver.find_element_by_id("id_valid_to_0")
       elem.send_keys("2019-08-10")
       time.sleep(2)

       elem = driver.find_element_by_id("id_valid_to_1")
       elem.send_keys("12:00:00")
       time.sleep(2)

       elem = driver.find_element_by_id("id_discount")
       elem.send_keys("10")
       time.sleep(2)

       elem = driver.find_element_by_id("id_active")
       elem.click()
       time.sleep(2)

       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       time.sleep(2)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()