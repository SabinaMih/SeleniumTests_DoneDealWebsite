import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest

class test_search_functionality(unittest.TestCase):
    chrome_browser = ""
    app_url = ""
    
    def setUp(self):
        self.chrome_webbrowser = webdriver.Chrome("UAT_WebDriver\chromedriver.exe")
        # Go and get the html
        self.app_url = "https://www.donedeal.ie/"

    def tearDown(self):
        # close the web browser
        self.chrome_webbrowser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.chrome_webbrowser.quit()
        
    def test_search_functionality_Succesful_inChrome(self):
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
        self.chrome_webbrowser.implicitly_wait(4)
        user_login = self.chrome_webbrowser.find_element_by_partial_link_text('Log in')
        user_login.click()

        user_email = self.chrome_webbrowser.find_element_by_id('email')
        user_password = self.chrome_webbrowser.find_element_by_id('password') 
        if user_email.is_displayed() and user_password.is_displayed():
            # enter user email
            user_email.send_keys("sabinam@gmail.com")
            user_password.send_keys("donedeaL2020" + Keys.RETURN)
        
        # click on the loup icon for the search function
        search_btn1 = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/a[1]/i')
        self.chrome_webbrowser.execute_script("arguments[0].click()", search_btn1)

        # perform an search without text inserted
        search_btn2 = self.chrome_webbrowser.find_element_by_xpath('//*[@id="modal-bg"]/div/div/div/form/div/div/button/i').click()
        #self.chrome_webbrowser.execute_script("arguments[0].click()", search_btn2)

        # store the expected title of the webpage.
        expected_title = "All Sections For Sale in Ireland | DoneDeal" 
        # actual title on Web Page
        actual_title = self.chrome_webbrowser.title
    
        # verify title and display the actual title
        if expected_title != actual_title:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_title )
        # assert (stop the test)
        assert expected_title in actual_title

        # check if the searched category is displayed in the breadcrumbmenu
        expected_categ_name = "All Sections" 
        actual_categ_name = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchHeaderPanel"]/div/div/div[1]/nav/ul/li[2]/a/span').text
        if expected_categ_name != actual_categ_name:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_categ_name )
            
            
        
        # perform a search with input
        user_search = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchHeaderPanel"]/div/div/div[2]/div[2]/div/input')
        user_search.send_keys("makeup")
        #click on the search button
        search_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchHeaderPanel"]/div/div/div[2]/div[2]/div/button/i').click()
        #self.chrome_webbrowser.execute_script("arguments[0].click()", search_btn)

        # check if the url changed 
        self.app_url = "https://www.donedeal.ie/all?words=makeup"
        if self.chrome_webbrowser.current_url != self.app_url:
            print("Verification fail the url displayed is" + str(self.chrome_webbrowser.current_url))
        # assert self.app_url in self.chrome_webbrowser.current_url

        # click on the save search button
        save_search_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[2]/div[3]/div/div/button').click()
        save_search_none_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[2]/div[3]/div/div/saved-search-popout/div/div[2]/label[3]/span').click()
        save_search_save_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[2]/div[3]/div/div/saved-search-popout/div/button').click()
        self.chrome_webbrowser.implicitly_wait(4)
        # access the seaved search from the menu
        user_name_btn = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/a[3]/span[2]').click()
        user_saved_search_btn = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/div[2]/ul/li[5]/a').click()
        user_search = self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/article/ul/li/a/dl').click()

        # filter menu for makeup search
        # location
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[1]/ng-switch/div/button/span[1]').is_displayed:
            self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[1]/ng-switch/div/button/span[1]').click()
            # select location from the list
            location_list = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[1]/ng-switch/div/div/div/header/a[1]')
            location_pref1 = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[1]/ng-switch/div/div/div/ul/li[15]/label/span').click()
            location_pref1 = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[1]/ng-switch/div/div/div/ul/li[19]/label/span').click()
            save_location_pref_btn= self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[1]/ng-switch/div/div/div/footer/button').click()
            # check if the location name changed
            expected_location_name = "Dublin (+1)" 
            actual_location_name = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[1]/ng-switch/div/button').text
            if expected_location_name != actual_location_name:
                print("Verification Failed - An incorrect location is displayed: " + actual_location_name)
                
        # price
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[2]/h6/label/span[2]').is_displayed:
            self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[2]/ng-switch/div/div/select').click()
            # select currency from the list
            user_price_currency = Select(self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[2]/ng-switch/div/div/select'))
            user_price_currency.select_by_visible_text('€')
            min_price = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[2]/ng-switch/div/input[1]')
            min_price.clear()
            min_price.send_keys(10)
            max_price = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[2]/ng-switch/div/input[2]')
            max_price.clear()
            max_price.send_keys(50)
        
        # seller type
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[3]/h6/label/span[2]').is_displayed:
            self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[3]/ng-switch/div/label[2]/span').click()
        
        # for sale / wanted
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[4]/h6/label').is_displayed:
            self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[4]/ng-switch/div/label[1]/span').click()
        
        # Sort
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[5]/h6/label/span[2]').is_displayed:
            self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[5]/ng-switch/div/div/select').click()
            # select low price from the list
            sort_low_price = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[5]/ng-switch/div/div/select').click()
        
        # view
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[6]/h6/label/span[2]').is_displayed:
            self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/ul/li[6]/ng-switch/div/label[2]/span').click()
        
        done_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[1]/div[2]/div/div/label').click()
        save_search_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[2]/div[3]/div/div/button').click()
        save_search_none_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[2]/div[3]/div/div/saved-search-popout/div/div[2]/label[3]/span').click()
        save_search_save_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[2]/div[3]/div/div/saved-search-popout/div/button').click()
        self.chrome_webbrowser.implicitly_wait(4)
        # check is the save search button is dissabled after the ad is saved
        if not self.chrome_webbrowser.find_element_by_xpath('//*[@id="searchContent"]/div[2]/div[3]/div/div/button').click():
            print("Success! The save search button is disables.")

         # access the seaved search from the menu
        # access the seaved search from the menu
        user_name_btn = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/a[3]/span[2]').click()
        user_saved_search_btn = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/div[2]/ul/li[5]/a').click()
        # check if the filters appear in the heading
        expected_saved_search_makeup = "All Sections, Dublin, Kildare, €10-€50, Private, For Sale"
        actual_saved_search_makeup = self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/article/ul/li[1]/a/dl/dd').text
        if expected_saved_search_makeup != actual_saved_search_makeup:
            print("Error" + actual_saved_search_makeup)

        # delete the first search 
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/article/ul/li[2]/a/dl/dd').is_displayed:
            first_search_del_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/article/ul/li[2]/div[2]/button').click()
            
        self.chrome_webbrowser.implicitly_wait(4)
# END