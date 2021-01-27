import unittest
from time import sleep
from selenium import webdriver
from login_page import LoginPage
from first_page import FirstPage
from addEnterprise_page import EntPage
from selenium.webdriver.support.ui import WebDriverWait


class TestBaiduPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def test_login(self):
        page = LoginPage(self.driver)
        page.get("http://testadmin.huxin315.com/user/login")
        self.driver.set_window_size(1936, 1056)
        page.server_button.click()
        page.server_selector.click()
        page.testServer_option.click()
        page.mobileLogin_button.click()
        page.mobile_input[0].click()
        page.mobile_input[0].send_keys("15176128570")
        page.verificationCode_input[1].send_keys("000000")
        page.login_button.click()
        sleep(5)
        #self.assertEqual(page.get_title(), "selenium_百度搜索")


    def test_addEnterprise(self):
        page = FirstPage(self.driver)
        sleep(10)
        element = WebDriverWait(self.driver, 10).until(lambda driver: page.addEnterprise_button)
        page.addEnterprise_button.click()
        pagee = EntPage(self.driver)
        pagee.button1.click()
        pagee.entName_input.click()
        pagee.entName_input.send_keys("公司名称")
        pagee.principal_input.click()
        pagee.principal_input.send_keys("12345678901234")
        pagee.busiModel_input.click()
        pagee.busiModel_option.click()
        pagee.industry_input.click()




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()