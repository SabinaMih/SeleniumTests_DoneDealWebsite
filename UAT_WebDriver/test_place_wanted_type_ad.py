import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest

class test_PlaceWantedTypeAd(unittest.TestCase):
    chrome_browser = ""
    app_url = ""
    
    def setUp(self):
        self.chrome_webbrowser = webdriver.Chrome("UAT_WebDriver\chromedriver.exe")
        # Go and get the html
        self.app_url = "https://www.donedeal.ie/publish"

    def tearDown(self):
        # close the web browser
        self.chrome_webbrowser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.chrome_webbrowser.quit()
        
    def test_PlaceWantedTypeAd_Succesfully_inChrome(self):
        # launch the chrome browser and open the application url
        self.chrome_webbrowser.get(self.app_url)

        # maximize the browser window
        self.chrome_webbrowser.maximize_window()

        # close and accept cookies policy 
        self.chrome_webbrowser.implicitly_wait(4)
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').is_displayed:
            cookie_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]')
            self.chrome_webbrowser.execute_script("arguments[0].click()", cookie_btn)

        #log in again check if name of input fields are displayed
        user_email = self.chrome_webbrowser.find_element_by_id('email')
        user_password = self.chrome_webbrowser.find_element_by_id('password') 
        if user_email.is_displayed() and user_password.is_displayed():
            # enter user email
            user_email.send_keys("sabinam@gmail.com")
            user_password.send_keys("donedeaL2020" + Keys.RETURN)
            
        # store the expected title of the webpage.
        expected_title = "Place an ad on Ireland's biggest classifieds site - DoneDeal.ie"

        # actual title on Web Page
        actual_title = self.chrome_webbrowser.title
      
        # verify title and display the actual title
        if expected_title != actual_title:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_title )
        # assert (stop the test)
        assert expected_title in actual_title
            
        
        # verify if the "Place Ad" link is displayed in the breadcrumb menu
        expected_link_name = "Place Ad"
        actual_link_name = self.chrome_webbrowser.find_element_by_class_name('oppa-page-title').text
        
        if expected_link_name != actual_link_name:
            print("Verification Failed - An incorrect link name is displayed on the bradcrumb menu: " + actual_link_name )
        # click on the "Wanted" button
        wanted_btn = self.chrome_webbrowser.find_element_by_id('wanted')
        self.chrome_webbrowser.execute_script("arguments[0].click()", wanted_btn)
        
        # check if the 'Ad Title' is displayed and insert a title if true
        ad_title = self.chrome_webbrowser.find_element_by_class_name('field-title')
        #print("user ad title " + str(ad_title.text))
        if ad_title.is_displayed():
            user_ad_title = self.chrome_webbrowser.find_element_by_id('ad-title')
            user_ad_title.clear()
            user_ad_title.send_keys("Looking for makeup.")

        # insert a price
        user_ad_price = self.chrome_webbrowser.find_element_by_id('price')
        user_ad_price.clear()
        user_ad_price.send_keys(10)
        
         # select currency
        user_price_currency = Select(self.chrome_webbrowser.find_element_by_id('currency'))
        user_price_currency.select_by_visible_text('€')
        
         # select a category
        user_categ = Select(self.chrome_webbrowser.find_element_by_id('section'))
        user_categ.select_by_visible_text('Clothes & Lifestyle')
        
        # select a category
        user_subcateg = Select(self.chrome_webbrowser.find_element_by_id('subsection'))
        user_subcateg.select_by_visible_text('Health & Beauty')

        # verify heading
        expected_desc_heading = "Add a Description"
        actual_desc_heading = self.chrome_webbrowser.find_element_by_xpath('//*[@id="adForm"]/div[11]/label').text
        #print(actual_desc_heading )
        if expected_desc_heading != actual_desc_heading:
            print("Verification Failed " + actual_desc_heading )
   
        # add a description 
        ad_desc = self.chrome_webbrowser.find_element_by_xpath('//*[@id="ad-desc"]')
        if ad_desc.is_displayed():
            user_ad_desc = self.chrome_webbrowser.find_element_by_id('ad-desc')
            user_ad_desc.clear()
            user_ad_desc.send_keys("I am looking for makeup.")

        # verify heading
        expected_plan_heading = "Choose your ad option"
        actual_plan_heading = self.chrome_webbrowser.find_element_by_xpath('//*[@id="cad-plan"]/label').text
    
        #print(actual_desc_heading )
        if expected_plan_heading != actual_plan_heading:
            print("Verification Failed " + actual_plan_heading )
       
        # click the "choose" button for free option 
        free_opt = self.chrome_webbrowser.find_element_by_xpath('//*[@id="upsell-package_Free"]/span[2]/span[1]')
        self.chrome_webbrowser.execute_script("arguments[0].click()", free_opt)

        
        # assert total to "free"
        expected_total = "FREE"
        actual_total = self.chrome_webbrowser.find_element_by_xpath('//*[@id="total"]/div/span').text
        
        if expected_total != actual_total:
            print("Error the actual total is:" + actual_total)

            assert expected_total in actual_total

         # assert name 
        expected_name = "You're logged in as Sabina Mihoc (sabinam@gmail.com)"
        actual_name= self.chrome_webbrowser.find_element_by_xpath('//*[@id="loggedin-details-holder"]/div[1]/div[1]/p').text
        assert expected_name in actual_name
        if expected_name != actual_name:
            print("Error the total should be:" + actual_name)
    
        
        # check autofill name field - not working
        expected_uname = "Sabina Mihoc"
        actual_uname= self.chrome_webbrowser.find_element_by_xpath('//*[@id="publisherNameSignup"]').text
        if actual_uname != expected_uname:
            print("Error the name is not filled in automaticaly" + actual_uname)
        
        # add phone num
        ad_phone = self.chrome_webbrowser.find_element_by_xpath('//*[@id="phoneInputContainer"]/label')
        if ad_phone.is_displayed():
            user_ad_phone = self.chrome_webbrowser.find_element_by_xpath('//*[@id="publisherPhoneSignup"]')
            user_ad_phone.clear()
            user_ad_phone.send_keys("0877059982")
        
        # select a county
        user_county = Select(self.chrome_webbrowser.find_element_by_id('county'))
        user_county.select_by_visible_text('Dublin')

        # select on "Nearest area" leave it blank
        user_county = Select(self.chrome_webbrowser.find_element_by_xpath('//*[@id="town"]'))
        
        # click on "Phone and text" button to cancel this option
        cancel_ph_op = self.chrome_webbrowser.find_element_by_xpath('//*[@id="loggedin-details-holder"]/div[1]/div[6]/label[2]/span')
        self.chrome_webbrowser.execute_script("arguments[0].click()", cancel_ph_op)

        # click on "I'm a trader" button to check if the additional 3 fields are displayed
        trader_op = self.chrome_webbrowser.find_element_by_xpath('//*[@id="loggedin-details-holder"]/div[1]/div[7]/label[2]/span')
        self.chrome_webbrowser.execute_script("arguments[0].click()", trader_op)

        # check if fields are displayed
        business_name = self.chrome_webbrowser.find_element_by_xpath('//*[@id="loggedin-details-holder"]/div[1]/div[8]/label')
        business_address = self.chrome_webbrowser.find_element_by_xpath('//*[@id="loggedin-details-holder"]/div[1]/div[9]/label/span')
        vat = self.chrome_webbrowser.find_element_by_xpath('//*[@id="loggedin-details-holder"]/div[1]/div[10]/label')
        if business_name.is_displayed() and business_address.is_displayed() and vat.is_displayed():
            print("Fields are displayed")
        time.sleep(4)
         # click on "I'm a trader" button again to cancel this option
        trader_op = self.chrome_webbrowser.find_element_by_xpath('//*[@id="loggedin-details-holder"]/div[1]/div[7]/label[2]/span')
        self.chrome_webbrowser.execute_script("arguments[0].click()", trader_op)

        # click on preview button
        preview = self.chrome_webbrowser.find_element_by_partial_link_text('Preview your ad').click()
        time.sleep(4)
        if preview:
            # click closed
            close_btn_prev = self.chrome_webbrowser.find_element_by_link_text('Close').click()
        
        # click on "Place Ad" button
        place_ad = self.chrome_webbrowser.find_element_by_xpath('//*[@id="ad-submit"]')
        self.chrome_webbrowser.execute_script("arguments[0].click()", place_ad)
        
        if place_ad:
            # click closed
            close_popup_sell_faster = self.chrome_webbrowser.find_element_by_css_selector('body > div.overlay.ng-scope > div > div > div.content-share-modal__body > a')
            self.chrome_webbrowser.execute_script("arguments[0].click()", close_popup_sell_faster)
            time.sleep(4)
        # check url 
        if self.app_url == self.chrome_webbrowser.current_url:
            view_ad = self.chrome_webbrowser.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[1]/div[2]/a[1]')
            self.chrome_webbrowser.execute_script("arguments[0].click()", view_ad)
            time.sleep(4)

        






