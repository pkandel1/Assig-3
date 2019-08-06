import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

class Customer_ATS(unittest.TestCase):


  def setUp(self):
       self.driver = webdriver.Chrome()

  def test_blog(self):
      my_list = read_mpg()
      user = "instructor"
      pwd = "instructor1a"
      driver = self.driver
      driver.maximize_window()
      driver.get("http://pkandel.pythonanywhere.com/admin")
      elem = driver.find_element_by_id("id_username")
      elem.send_keys(user)
      elem = driver.find_element_by_id("id_password")
      elem.send_keys(pwd)
      elem.send_keys(Keys.RETURN)
      driver.get("http://pkandel.pythonanywhere.com/admin")
      assert "Logged In"
      time.sleep(5)
      elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/th/a").click()
      for i in range(0, len(my_list)):


       my_list = read_mpg()
       elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
       time.sleep(5)
       Cust_name = my_list[i][0]
       Organization = my_list[i][1]
       Role = my_list[i][2]
       Email = my_list[i][3]
       BldgRoom = my_list[i][4]
       Address = my_list[i][5]
       Account_No = my_list[i][6]
       City = my_list[i][7]
       State = my_list[i][8]
       Zipcode = my_list[i][9]
       PhoneNumber = my_list[i][10]

       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys(Cust_name)

       elem = driver.find_element_by_id("id_organization")
       elem.send_keys(Organization)

       elem = driver.find_element_by_id("id_role")
       elem.send_keys(Role)

       elem = driver.find_element_by_id("id_email")
       elem.send_keys(Email)

       elem = driver.find_element_by_id("id_bldgroom")
       elem.send_keys(BldgRoom)

       elem = driver.find_element_by_id("id_address")
       elem.send_keys(Address)

       elem = driver.find_element_by_id("id_account_number")
       elem.send_keys(Account_No)

       elem = driver.find_element_by_id("id_city")
       elem.send_keys(City)

       elem = driver.find_element_by_id("id_state")
       elem.send_keys(State)

       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys(Zipcode)

       elem = driver.find_element_by_id("id_phone_number")
       elem.send_keys(PhoneNumber)

       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       time.sleep(4)
       


def read_mpg():
    File = "Book2.csv"
    my_list = []
    with open(File) as file:
        reader = csv.reader(file)
        for row in reader:
            my_list.append(row)
    return my_list

    test_blog()


if __name__ == "__main__":
   unittest.main()