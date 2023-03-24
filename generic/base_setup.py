import pytest
from selenium.webdriver import chrome
from selenium.webdriver.support.wait import WebDriverWait

class  Base_Setup:

     @pytest.fixture(autouse=True)
     def precondition(self):
         self.driver = Chrome()
         self.driver.get("http://www.google.com")
         self.driver.maximize_window()
         self.driver.implicitly.wait(10)
         self.wait=WebDriverWait(self.driver,10)


     @pytest.fixture(autouse=True)
     def precondition(self):
     self.driver.quit()