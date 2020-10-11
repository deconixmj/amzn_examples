# Let say some category related data is changed and new categories are added
# we want to make sure all categories are reachable from homepage.

import unittest
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage
from ddt import ddt,data,unpack
from TestData.read import get_categories
from datetime import datetime
import logging,time


@ddt
class ACPT(unittest.TestCase):
    # driver=""

    @classmethod
    def setUpClass(cls):
        url="https://www.amazon.in/"
        cls.base=BasePage(url)
        cls.home=HomePage(cls.base.driver)
        cls.home.click_on_categorymenu()
        logging.basicConfig(filename="TitleVerification.log",format='%(asctime)s :%(levelname)s: %(message)s',filemode='w')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)

    def setUp(self):
        pass
        # self.home.click_on_categorymenu()

        # L=get_categories()

    # @data(*get_categories())
    # @unpack

    def test_MobilesComputers_CategoryPageVerify(self):
        Titles=["Mobile Phones: Buy New Mobiles Online at Best Prices in India | Buy Cell Phones Online - Amazon.in",
                "Mobile Accessories: Buy Mobile Accessories online at best prices in India - Amazon.in",
                "Mobile Covers: Buy Mobile Cases Online at Best Prices in India - Amazon.in",
                "Mobile Screen Protector: Buy Mobile Phone Screen Protectors, Screen Guards & Scratch Guards Online at Low Prices in India: Amazon.in",
                "Power Bank: Buy Power Banks online at best prices in India - Amazon.in",
                "Computers & Accessories: Buy Computers & Accessories Online at Low Prices in India - Amazon.in",
                "Laptop Prices in India: Buy Laptops Online at Low Prices | Windows, Mac, DOS Laptops - Amazon.in"]

        L=get_categories()
        Test_titles=[]
        for catname in L[0]:
            self.home.click_on_category("7",catname)
            title1=ACPT.base.driver.title
            Test_titles.append(title1)
            # time.sleep(2)
            self.base.navigate_back()
            time.sleep(2)
            self.home.click_on_categorymenu()
            # time.sleep(2)

        # print(Test_titles)
        for i in range(len(Test_titles)):
            with self.subTest(i=i):
                try:
                    self.assertEqual(Titles[i], Test_titles[i], "category title did not match")
                    logging.info("Category title verification pass: {}".format(Test_titles[i], Titles[i]))

                except AssertionError:
                    logging.error("Category title verification failed: {}".format(Test_titles[i], Titles[i]))




            # assert title  == ACPT.base.driver.title , "Category title did not match"

    def tearDown(self):
        pass
        # ssname = 'ss_' + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.png'
        # cls.base.driver.save_screenshot('D:\\amzn_testcases\Reports\Screenshots\%s' % ssname)
        # # self.driver.save_screenshot()

    @classmethod
    def tearDownClass(cls):
        # quit()
        ACPT.base.driver.close()

        # self.base.driver.close()