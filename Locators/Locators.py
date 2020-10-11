from selenium.webdriver.common.by import By

class HomePageLocators:
    """
    """

class CategoryLocators:
    def __init__(self,category_str,category_str1):

        # self.id=category_str
        self.m_c=(By.XPATH,"//a[@data-menu-id='" + category_str + "']")
        self.s_c=(By.XPATH,"//a/div[contains(text(),'" + category_str1 + "')]")
        # self.s_c=(By.LINK_TEXT,category_str1)

    CategoryMenu=(By.ID,"nav-hamburger-menu")

    # def main_category(self,main_category_str):
    #
    #     # for i in range(0,19):
    #     id=str(range(0,19))
    #     main_category=(By.XPATH,"//a[@data-menu-id=id")

