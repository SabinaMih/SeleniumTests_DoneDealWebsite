import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest

class test_price_assist_functionality(unittest.TestCase):
    chrome_browser = ""
    app_url = ""
    
    def setUp(self):
        self.chrome_webbrowser = webdriver.Chrome("UAT_WebDriver\chromedriver.exe")
        # Go and get the html
        self.app_url = "https://priceassist.donedeal.ie/"

    def tearDown(self):
        # close the web browser
        self.chrome_webbrowser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.chrome_webbrowser.quit()
        
    def test_price_assist_functionality_Succesful_inChrome(self):
        # launch the chrome browser and open the application url
        self.chrome_webbrowser.get(self.app_url)

        # maximize the browser window
        self.chrome_webbrowser.maximize_window()

        # click on car valuation button 
        #car_val_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="js-homepage-content"]/div/div[4]/div/ul/li[4]/a/h2').click()
        self.chrome_webbrowser.implicitly_wait(4)
        # store the expected title of the webpage.
        expected_title_p = "Price Assist" 
        # actual title on Web Page
        actual_title_p = self.chrome_webbrowser.title
    
        # verify title and display the actual title
        if expected_title_p != actual_title_p:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_title_p)
        # assert (stop the test)
        assert expected_title_p in actual_title_p

        # insert invalid reg number
        user_reg_num = self.chrome_webbrowser.find_element_by_xpath('//*[@id="registration-number-string-id"]')
        user_reg_num.send_keys("162-Z-31404")
        check_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="submitRegistrationNumberButton"]').click()

        #check if the not found message appears on the page
        expected_not_found_msg = "Not Found"
        actual_not_found_msg = self.chrome_webbrowser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/h1').text
        if expected_not_found_msg != actual_not_found_msg:
            print("Error a different message is displayed on the page" + actual_not_found_msg)
        
        #click on the back button
        back_btn = self.chrome_webbrowser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/a').click()

        # insert valid reg number and odometer
        user_reg_num = self.chrome_webbrowser.find_element_by_xpath('//*[@id="registration-number-string-id"]')
        user_reg_num.send_keys("162-D-31404")
        odometer = self.chrome_webbrowser.find_element_by_xpath('//*[@id="odometer-string-id"]')
        odometer.send_keys("100000")
        check_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="submitRegistrationNumberButton"]').click()
        
        #check if the correct car name is returned
        expected_car = "How your Ford Focus 2016 100,000 km compares"
        actual_car = self.chrome_webbrowser.find_element_by_xpath('//*[@id="marketAverageWidget"]/div[1]/div/div/div[2]/h4').text
        if expected_car != actual_car:
            print("Error a different car info is displayed on the page" + actual_car)
        
         #click on the back button
        back_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="backButton"]').click()

        # get average price without having an registration number
        user_make = self.chrome_webbrowser.find_element_by_xpath('//*[@id="priceAssistForm"]/div[2]/div/button').click()
        user_make_s = self.chrome_webbrowser.find_element_by_xpath('//*[@id="priceAssistForm"]/div[2]/div/div/ul/li[12]/a/span[1]/small').click()

        self.chrome_webbrowser.implicitly_wait(4)
        # check if the field is dissabled if the previews field is not selected
        if not self.chrome_webbrowser.find_element_by_xpath('//*[@id="priceAssistForm"]/div[4]/div/button/span[1]').click():
            print("This option is disabled until the previews field is selected!")
        
        md_of_the_car = self.chrome_webbrowser.find_element_by_xpath('//*[@id="priceAssistForm"]/div[3]/div/button/span[1]').click()
        md_of_the_car_sel = self.chrome_webbrowser.find_element_by_xpath('//*[@id="priceAssistForm"]/div[3]/div/div/ul/li[6]/a/span[1]')
        md_of_the_car_sel = self.chrome_webbrowser.execute_script("arguments[0].click()", md_of_the_car_sel)
        check_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="submitButton"]').click()
        self.chrome_webbrowser.implicitly_wait(4)


        

      