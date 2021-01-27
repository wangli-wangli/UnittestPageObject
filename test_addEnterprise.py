import unittest
from time import sleep
from selenium import webdriver



class TestPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #def test_login(self):


if __name__ == '__main__':
    unittest.main()

