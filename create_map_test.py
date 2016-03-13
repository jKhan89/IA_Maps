from selenium import webdriver
import unittest
import HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.webfocus.webfocus import WF_Functions


#tell unittest module that this is a test case
class CreateMap(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_choro_map(self):
        #set up driver and URL
        driver = self.driver
        driver.get('http://bigscm13:26000/ibi_apps/')


        #new WF_Fucntions instance
        wf = WF_Functions(driver)
        time.sleep(3)

        #call login function
        wf.login('manager','manager')

        #Commented out creating domain. Add in code if needed
        #wf.create_domain('jk_test')

        
        #Launch IA Chart
        wf.launch_chart('jk_test')
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])

        #Select app and master file. Change accordingly
        wf.select_data('jk_test','country_population.mas')

        #Check to make sure IA Chart is opened
        #if WF_Functions(driver).is_visible('#pfjChart_1 > svg'):
        #    print('IA Chart opened')


        #Select choropleth map
        wf.select_tab('format')
        wf.select_chart('choropleth')

        #replace variables with specific field names based on master file
        wf.add_field_to_default('country name')
        time.sleep(4)
        wf.add_field_to_default('population')
        time.sleep(4)

        #Run the chart
        wf.runQuery()

        #Save the chart
        wf.quickSave('Choropleth Map1')


        #Exit IA and return to BI Portal
        driver.close()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[0])

        #Edit the saved fex
        wf.editFex('Choropleth Map1')
        time.sleep(12)


        #Verify and close IA
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

    def test_bubble_map(self):
        driver = self.driver
        driver.get('http://bigscm13:26000/ibi_apps/')

        
        wf = WF_Functions(driver)

        wf.login('manager','manager')
        time.sleep(6)

        wf.launch_chart('jk_test')
        time.sleep(3)
        driver.switch_to_window(driver.window_handles[1])

        #Select app and master file. Change accordingly
        wf.select_data('jk_test','country_population.mas')

        #Check to make sure IA Chart is opened
        #if WF_Functions(driver).is_visible('#pfjChart_1 > svg'):
        #    print('IA Chart opened')


        #Select bubble map
        wf.select_tab('format')
        wf.select_chart('proportional symbol')


        #replace variables with specific field names based on master file
        wf.add_field_to_default('country name')
        time.sleep(4)
        wf.add_field_to_default('population')
        time.sleep(4)

        
        #Run the chart
        wf.runQuery()
        
        #Save the chart
        wf.quickSave('Bubble Map1')

        #Exit IA and return to BI Portal
        driver.close()
        time.sleep(1)
        driver.switch_to_window(driver.window_handles[0])


        #Edit the saved fex
        wf.editFex('Bubble Map1')
        time.sleep(12)


        #Verify and close IA
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

#    def test_failure(self):
#        driver = self.driver
#        driver.get('http://bigscm13:26000/ibi_apps/')
#
#        wf = WF_Functions(driver)
#
#        wf.login('manager','manager')
#        time.sleep(6)
#
#        wf.launch_chart('jk_test1')
#        time.sleep(3)


    #Tear down session
    def tearDown(self):
        self.driver.quit()


suite = unittest.TestLoader().loadTestsFromTestCase(CreateMap)
unittest.TextTestRunner(verbosity=2)
with open("results.html","w") as output:
    runner = HTMLTestRunner.HTMLTestRunner(stream=output,title='Automation Results',description='Test Results for creating Choropleth and Bubble maps in 8200')
    runner.run(suite) 
