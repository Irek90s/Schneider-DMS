from selenium import  webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Test():
    def __init__(self):
        self.login_url = "http://127.0.0.1/K3Cloud/html5/dform.aspx?formId=BOS_HtmlConsole&formType=mobileform&pageId=9d49a246-5d99-4842-a470-8ad60fc7726b&usertoken=10d2b83d-dc7a-466f-a270-0b867b477ed5"
        self.driver = webdriver.Chrome()
    def login(self, xpath):
        self.driver.get(self.login_url)
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='CloudAllFunctionBtn']").click()
        count = 0
        while True:
            try:
                # WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located((By.XPATH, xpath)))    
                # WebDriverWait(self.driver, 60, 1).until(EC.alert_is_present())    
            except Exception:
                print("*"*50)
                self.driver.refresh()
            else:
                self.driver.find_element_by_xpath("//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_span']")
                print("#"*50)
            count = count + 1
            if count == 5:
                break
              
              

test = Test()
test.login("//span[@id='BOS_MainSystemMenu-FSYSTEMTREEVIEW_c_23_span']")

