from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class ESRI(object):
    def __init__(self, driver):
        self.driver = driver

    def zoom_in(self):
                zInBtn = self.driver.find_element_by_class_name("esriSimpleSliderIncrementButton")
                ActionChains(self.driver).click(zInBtn).perform()

    def zoom_out(self):
                zOutBtn = self.driver.find_element_by_class_name("esriSimpleSliderDecrementButton")
                ActionChains(self.driver).click(zOutBtn).perform()

    def change_basemap(self, basemap_name):
        basemap_btn = self.driver.find_element_by_id("dijit_TitlePane_0")
        ActionChains(self.driver).click(basemap_btn).perform()
        basemap = self.driver.find_element_by_xpath('//*[@title="%s"]' %basemap_name)
        ActionChains(self.driver).click(basemap).perform()
        widget_btn = self.driver.find_element_by_id("dijit_TitlePane_1_titleBarNode")
        ActionChains(self.driver).click(widget_btn).perform()
                
    def find_bubble(self,value):
        map_layer = self.driver.find_element_by_id('layerId_0_layer')
        bubble = map_layer.find_element_by_xpath('.//*[contains(@tdgtitle, ">%s<")]' %value)
        return bubble

    def hover_over_bubble(self, val):
        point = ESRI(self.driver).find_bubble(val)
        ActionChains(self.driver).move_to_element(point).perform()

    def zoom_on_point(self, val, levels):
        i = 0
        while i < levels:
            point = ESRI(self.driver).find_bubble(val)
            ActionChains(self.driver).double_click(point).perform()
            time.sleep(2)
            i = i+1

    def toggle_main_layer(self):
        layer = self.driver.find_element_by_css_selector('.TableOfContentsButton.UIButton')
        ActionChains(self.driver).click(layer).perform()
        time.sleep(1)
        vis_layers = self.driver.find_elements_by_class_name('toc-title')
        main_layer = vis_layers[0]
        ActionChains(self.driver).click(main_layer).perform()
        time.sleep(1)
        layer_open = self.driver.find_element_by_class_name('toc-header')
        ActionChains(self.driver).click(layer_open).perform()
        time.sleep(1)
    

    
            

    
    
    

    
        
        
