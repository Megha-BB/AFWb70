from generic.base_setup import Base_Setup

class  TestScript1(BaseSetup):

    def test_script(self):
        print("this is script 1")
        print(self.driver.title)
