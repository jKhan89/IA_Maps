from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.webfocus.webfocus import WF_Functions
import time


class LaunchIA(object):
    def __init__(self,driver):
        self.driver = driver

    def validate_tool(self):
        time.sleep(2)
        if len(self.driver.window_handles) == 2:
            self.driver.switch_to_window(self.driver.window_handles[1])
        WF_Functions(self.driver).is_visible('#paneIbfsExplorer_exTree > div.bi-tree-view-body-content > table > tbody')
        
    def Report(self):
        ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT).perform()
        validate_tool(self)

    def Chart(self):
        ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT,Keys.DOWN).perform()
        validate_tool(self)

    def Document(self):
        ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.DOWN).perform()
        validate_tool(self)

        
    def Dashboard(self):
        ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT,Keys.DOWN,Keys.DOWN).perform()
        validate_tool(self)

    def Visualization(self):
        ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN).perform()
        validate_tool(self)
    
