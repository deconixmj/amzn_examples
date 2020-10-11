from selenium import webdriver
import time

from Locators.Locators import CategoryLocators,HomePageLocators

# x=CategoryLocators()
# x=CategoryLocators(category_str,category_str1)

class HomePage:
    driver=""
    # m_c=""

    def __init__(self,d):
        self.driver=d

    def click_on_categorymenu(self):

        self.driver.find_element(*CategoryLocators.CategoryMenu).click()

    def click_on_category(self,category_str,category_str1):

        # self.cstr=self.m_c
        x = CategoryLocators(category_str, category_str1)
        self.driver.find_element(*x.m_c).click()
        time.sleep(3)
        self.driver.find_element(*x.s_c).click()


