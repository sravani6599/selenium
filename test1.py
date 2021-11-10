import selenium
from selenium import webdriver

class Autolog:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get("http://www.practiceselenium.com/welcome.html")


test =Autolog()
test.login()