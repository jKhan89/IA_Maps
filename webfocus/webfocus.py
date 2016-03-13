from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
import time


class WF_Functions(object):
        def __init__(self, driver):
                self.driver = driver

        def login(self, username, password):
                self.driver.find_element_by_id("SignonUserName").send_keys(username)
                self.driver.find_element_by_id("SignonPassName").send_keys(password)
                self.driver.find_element_by_id("SignonbtnLogin").click()
                WF_Functions(self.driver).is_visible('body > div.idis-administrator')
                

        def create_folder(self, name, summary):
                content = self.driver.find_element_by_xpath('//*[contains(text(), "Content") and @class=" sort-column"]')
                ActionChains(self.driver).move_to_element_with_offset(content, 20, 3).context_click().perform()
                time.sleep(1)
                ActionChains(self.driver).send_keys('\ue015','\ue015').perform()
                ActionChains(self.driver).send_keys(Keys.RIGHT).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()
                self.driver.implicitly_wait(2)
                fold_name = self.driver.find_element_by_xpath('//*[@id="newdesc"]')
                fold_summ = self.driver.find_element_by_xpath('//*[@id="newsummary"]')
                fold_name.send_keys(name)
                fold_summ.send_keys(summary)
                ActionChains(self.driver).move_to_element(fold_summ).click().perform()
                ActionChains(self.driver).send_keys('\ue004').send_keys('\ue006').perform()

        def create_sub_folder(self, parent, name, summary):
                p_folder = self.driver.find_element_by_xpath('//*[contains(text(), "%s") and @class=" sort-column"]' %parent)
                ActionChains(self.driver).move_to_element_with_offset(p_folder, 30, 3).context_click().perform()
                ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT).perform()
                ActionChains(self.driver).send_keys(Keys.UP, Keys.UP).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()
                #needs code to enter name and summary, then validate


        def launch_chart(self, folder):
                p_folder = self.driver.find_element_by_xpath('//*[contains(text(), "%s") and @class=" sort-column"]' %folder)
                ActionChains(self.driver).move_to_element_with_offset(p_folder, 30, 3).context_click().perform()
                time.sleep(1)
                ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT,Keys.DOWN).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()
                #ok_btn = self.driver.find_element_by_id("btnOK")
                #ActionChains(self.driver).click(ok_btn).perform()
                time.sleep(2)
                if len(self.driver.window_handles) == 2:
                        self.driver.switch_to_window(self.driver.window_handles[1])

        def select_tab(self,name):
                tab_lower = name.lower()
                tab_name = tab_lower.title()
                tab_id = self.driver.find_element_by_id("%sTab_tabButton" %tab_name)
                ActionChains(self.driver).click(tab_id).perform()

        def select_chart(self,chart):
                lower_chart = chart.lower()
                chart_name = lower_chart.title()
                if chart_name == "Proportional Symbol":
                        chart_name = "BubbleMap"
                if WF_Functions(self.driver).is_visible('#FormatBarChart'):
                        chart_id = self.driver.find_element_by_id("Format%sChart" %chart_name)
                        ActionChains(self.driver).click(chart_id).perform()

        def is_visible(self, locator, timeout=15):
                try:
                        ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
                        return True
                except TimeoutException:
                        return False
        def launch_text(self, folder):
                p_folder = self.driver.find_element_by_xpath('//*[contains(text(), "%s") and @class=" sort-column"]' %folder)
                ActionChains(self.driver).move_to_element_with_offset(p_folder, 30, 3).context_click().perform()
                ActionChains(self.driver).send_keys(Keys.DOWN, Keys.RIGHT,Keys.UP,Keys.UP,Keys.UP,Keys.UP,Keys.UP,Keys.UP,Keys.UP).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()

        def upload_doc(self, folder, path_to_file):
                p_folder = self.driver.find_element_by_xpath('//*[contains(text(), "%s") and @class=" sort-column"]' %folder)
                ActionChains(self.driver).move_to_element_with_offset(p_folder, 30, 5).context_click().perform()
                time.sleep(2)
                ActionChains(self.driver).send_keys(Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.RIGHT,Keys.DOWN).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()
                dialog = self.driver.find_element_by_css_selector('.bi-component.group-box-container')
                comps = dialog.find_elements_by_css_selector('.bi-component')
                comps[1].send_keys("%s" %path_to_file)
                time.sleep(2)
                upld_btn = self.driver.find_element_by_id('btnSubmit')
                ActionChains(self.driver).move_to_element(upld_btn).click().perform()
                WF_Functions(self.driver).is_visible('.bi-button.button.button-focus')
                ok=self.driver.find_element_by_css_selector('.bi-button.button.button-focus')
                ActionChains(self.driver).click(ok).perform()

        def run_item(self, folder, item):
                p_folder = self.driver.find_element_by_xpath('//*[contains(text(), "%s") and @class=" sort-column"]' %folder)
                item_ = p_folder.find_element_by_xpath('//*[contains(text(), "%s")]' %item)
                ActionChains(self.driver).move_to_element_with_offset(item_, 60, 5).context_click().perform()
                time.sleep(1)
                ActionChains(self.driver).send_keys(Keys.DOWN).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()

        def create_domain(self, domain_name):
                domain = self.driver.find_element_by_xpath('//*[contains(text(), "Domains") and @class=" sort-column"]')
                ActionChains(self.driver).move_to_element_with_offset(domain, 20, 3).context_click().perform()
                time.sleep(1)
                ActionChains(self.driver).send_keys(Keys.DOWN, Keys.DOWN, Keys.RIGHT).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()
                time.sleep(2)
                title_ = self.driver.find_element_by_css_selector('.bi-text-field.text-field.text-field-focus')
                ActionChains(self.driver).click(title_).perform()
                ActionChains(self.driver).send_keys(domain_name).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()
                time.sleep(4)
                ok = self.driver.find_element_by_css_selector('.bi-button.button.button-focus')
                ActionChains(self.driver).click(ok).perform()

        def select_data(self, app_name, data_file):
                if WF_Functions(self.driver).is_visible('#paneIbfsExplorer_exTree > div.bi-tree-view-body-content > table > tbody'):
                        app_container = self.driver.find_element_by_xpath('//*[@id="paneIbfsExplorer_exTree"]/div[2]/table/tbody')
                        app = app_container.find_element_by_xpath('//td[contains(text(),"%s")]' %app_name)
                        ActionChains(self.driver).move_to_element_with_offset(app,50,4).click().perform()
                        if WF_Functions(self.driver).is_visible('#IbfsOpenFileDialog7_cbFileName'):
                                file_box = self.driver.find_element_by_id('IbfsOpenFileDialog7_cbFileName')
                                ActionChains(self.driver).click(file_box).perform()
                                ActionChains(self.driver).send_keys("%s" %data_file).perform()
                                time.sleep(2)
                                ActionChains(self.driver).send_keys('\ue006').perform()

        def add_field_to_default(self,field_name):
                srch_fld = self.driver.find_element_by_id('metaDataSearchTxtFld')
                ActionChains(self.driver).click(srch_fld).send_keys("%s" %field_name).perform()
                field = self.driver.find_elements_by_xpath('//*[@id="QbMetaDataTree-1779"]/div[2]/table/tbody/tr[1]')
                if len(field) == 1:
                        ActionChains(self.driver).move_to_element_with_offset(field[0],40,5).double_click().perform()
                        srch_fld.clear()
                else:
                        print('Error selecting field. Ensure correct spelling and input entire field name')

        def runQuery(self):
                run_btn = self.driver.find_element_by_id('runButton')
                ActionChains(self.driver).click(run_btn).perform()
                time.sleep(10)

        def quickSave(self,title):
               saveBtn = self.driver.find_element_by_id('saveButton')
               ActionChains(self.driver).click(saveBtn).perform()
               if WF_Functions(self.driver).is_visible('#paneIbfsExplorer',3):
                       title_box = self.driver.find_element_by_css_selector('#IbfsOpenFileDialog7_cbFileName')
                       ActionChains(self.driver).click(title_box).perform()
                       ActionChains(self.driver).double_click().send_keys(Keys.DELETE).perform()
                       ActionChains(self.driver).send_keys("%s" %title).perform()
                       ActionChains(self.driver).send_keys('\ue006').perform()
               else:
                       ActionChains(self.driver).send_keys('\ue006')

        def editFex(self,fex_name):
                fex = self.driver.find_element_by_xpath('//*[contains(text(), "%s") and @class=" sort-column"]' %fex_name)
                ActionChains(self.driver).move_to_element_with_offset(fex, 50, 5).context_click().perform()
                time.sleep(1)
                ActionChains(self.driver).send_keys(Keys.DOWN, Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN,).perform()
                ActionChains(self.driver).send_keys('\ue006').perform()
                time.sleep(5)
                self.driver.switch_to_window(self.driver.window_handles[1])
        
        def expand_domain(domain_name):
                p_folder = self.driver.find_element_by_xpath('//*[contains(text(), "%s") and @class=" sort-column"]' %folder)
                ActionChains(driver).double_click(p_folder)
        
