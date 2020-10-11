from selenium import webdriver

class BasePage:

    driver=""
    def __init__(self,url):
        self.driver=webdriver.Chrome("D:\\amzn_testcases\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(url)

    def navigate_back(self):
        self.driver.back()

