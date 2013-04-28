'''Acceptance test for Missing Registration Information.
This tests the system when someone tries to register 
without having all the required fields filled in with
informations.
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest

class FailReg(unittest.TestCase):
    '''
    defining the fail registration class
    '''
    def setUp(self):
        '''
        
        '''
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://lit-earth-8332.herokuapp.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_fail_reg(self):
        '''
        d
        '''
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("design")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
    def is_element_present(self, how, what):
        '''
        defining the function 
        '''
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        '''
        defining the function
        '''
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
