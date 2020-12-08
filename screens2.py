from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def auto(user1,user2):

    driver=webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    driver.get(r"C:\Users\sravanti\Desktop\cg 2019\index.html")
    elem=driver.find_element_by_name('tq')
    elem1=driver.find_element_by_name('tq1')
    elem.clear()
    elem1.clear()

    elem.send_keys(user1)
    elem1.send_keys(user2)
    elem.send_keys(Keys.RETURN)
    elem1.send_keys(Keys.RETURN)
   
