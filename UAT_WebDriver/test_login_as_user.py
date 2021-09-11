import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class test_UserLogin_in_chrome(unittest.TestCase):
    chrome_browser = ""
    app_url = ""
    
    def setUp(self):
        self.chrome_webbrowser = webdriver.Chrome("UAT_WebDriver\chromedriver.exe")
        # Go and get the html
        self.app_url = "https://www.donedeal.ie"


    def tearDown(self):
        # close the web browser
        self.chrome_webbrowser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.chrome_webbrowser.quit()
        

    def test_userLoginSuccessfully_inChrome(self):
        # launch the chrome browser and open the application url
        self.chrome_webbrowser.get(self.app_url)

        # maximize the browser window
        self.chrome_webbrowser.maximize_window()
        
        # close and accept cookies policy 
        self.chrome_webbrowser.implicitly_wait(4)
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').is_displayed:
            cookie_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]')
            self.chrome_webbrowser.execute_script("arguments[0].click()", cookie_btn)

        # store the expected title of the webpage.
        expected_title = "DoneDeal | Ireland's Largest Motor & Classifieds Marketplace"

        # actual title on Web Page
        actual_title = self.chrome_webbrowser.title
     
        # assert title and display the actual title
        #display the error messege before the assert in case the assert stops the test
        if expected_title != actual_title:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_title )
            # assert (stop the test)
        assert expected_title in actual_title
        
        #verify the "Log in"
        expected_heading = "Log in"
        # actual title on Web Page
        actual_heading = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/div[1]/a[1]').text
        if expected_heading != actual_heading:
            print("Verification Failed - An incorrect heading is displayed on the web page: " + actual_heading)
            
        user_login = self.chrome_webbrowser.find_element_by_partial_link_text('Log in')
        user_login.click()
        # check if name of input fields are displayed
        user_email = self.chrome_webbrowser.find_element_by_name('email')
        user_password = self.chrome_webbrowser.find_element_by_name('password') 
        if user_email.is_displayed() and user_password.is_displayed():
            # enter user email
            user_email.send_keys("sabinam@gmail.com")
            user_password.send_keys("donedeaL2020" + Keys.RETURN)
            
        # verify if user name is displayed
        time.sleep(6)   # wait for the pop up to dissapear before checking the user name
        expected_user_name = "Sabina"
        actual_user_name = self.chrome_webbrowser.find_element_by_partial_link_text('Sabina').text
        
        if expected_user_name != actual_user_name:
            print("Verification Failed - An incorrect user name is displayed on the web page: " + actual_user_name )
        # click on the user name menu
        user_name = self.chrome_webbrowser.find_element_by_partial_link_text('Sabina').click()
        user_name_profile = self.chrome_webbrowser.find_element_by_partial_link_text('My DoneDeal').click()
        # check if brought to profile page
        user_profile_url = "https://www.donedeal.ie/accounts/classifieds/mydonedeal"
        if self.chrome_webbrowser.current_url != user_profile_url:
            print("Wrong page loaded")
        # check user name in profile page
        expected_user_pname = "Sabina"
        actual_user_pname = self.chrome_webbrowser.find_element_by_class_name('header-menu-name').text
    
        if expected_user_pname != actual_user_pname:
            print("Verification Failed - An incorrect user name is displayed on the profile page: " + actual_user_pname )


class test_UserLogin_in_FireFox(unittest.TestCase):
    firefox_browser = ""
    app_url = ""
    
    def setUp(self):
        self.firefox_webbrowser = webdriver.Firefox(executable_path=r"c:\\UAT_WebDriver\\geckodriver.exe")
        # Go and get the html
        self.app_url = "https://www.donedeal.ie"


    def tearDown(self):
        # close the web browser
        self.firefox_webbrowser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.firefox_webbrowser.quit()
        

    def test_userLoginSuccessfully_in_FireFox(self):
        # launch the chrome browser and open the application url
        self.firefox_webbrowser.get(self.app_url)

        # maximize the browser window
        self.firefox_webbrowser.maximize_window()
        
        # close and accept cookies policy 
        self.firefox_webbrowser.implicitly_wait(4)
        if self.firefox_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').is_displayed:
            cookie_btn = self.firefox_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]')
            self.firefox_webbrowser.execute_script("arguments[0].click()", cookie_btn)

        # store the expected title of the webpage.
        expected_title = "DoneDeal | Ireland's Largest Motor & Classifieds Marketplace"

        # actual title on Web Page
        actual_title = self.firefox_webbrowser.title
     
        # verify title and display the actual title
        if expected_title != actual_title:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_title )
            # assert (stop the test)
            assert expected_title in actual_title
        else:
            # check if the "Log in" link is displayed
            expected_link_name = "Log in"
            actual_link_name = self.firefox_webbrowser.find_element_by_partial_link_text('Log in').text
            assert expected_link_name in actual_link_name
            if expected_link_name != actual_link_name:
                print("Verification Failed - An incorrect link name is displayed on the web page: " + actual_link_name )
            
            user_login = self.firefox_webbrowser.find_element_by_partial_link_text('Log in')
            user_login.click()

            # step 4
            expected_heading = "Log in"
            # actual title on Web Page
            actual_heading = self.firefox_webbrowser.find_element_by_css_selector('h3.heading').text
            assert expected_heading in actual_heading 
            if expected_heading != actual_heading:
                print("Verification Failed - An incorrect heading is displayed on the web page: " + actual_heading)

            # check if name of input fields are displayed
            user_email = self.firefox_webbrowser.find_element_by_name('email')
            user_password = self.firefox_webbrowser.find_element_by_name('password') 
            if user_email.is_displayed() and user_password.is_displayed():
                # enter user email
                user_email.send_keys("sabinam@gmail.com")
                user_password.send_keys("donedeaL2020" + Keys.RETURN)
            
            # check if user name is displayed
            time.sleep(6)   # wait for the pop up to dissapear before checking the user name
            expected_user_name = "Sabina"
            actual_user_name = self.firefox_webbrowser.find_element_by_partial_link_text('Sabina').text
            assert expected_user_name in actual_user_name
            if expected_user_name != actual_user_name:
                print("Verification Failed - An incorrect user name is displayed on the web page: " + actual_user_name )
            # click on the user name menu
            user_name = self.firefox_webbrowser.find_element_by_partial_link_text('Sabina').click()
            user_name_profile = self.firefox_webbrowser.find_element_by_partial_link_text('My DoneDeal').click()
            # check if brought to profile page
            user_profile_url = "https://www.donedeal.ie/accounts/classifieds/mydonedeal"
            if self.firefox_webbrowser.current_url != user_profile_url:
                print("Wrong page loaded")
            # check user name in profile page
            expected_user_pname = "Sabina"
            actual_user_pname = self.firefox_webbrowser.find_element_by_class_name('header-menu-name').text
            assert expected_user_pname in actual_user_pname
            if expected_user_pname != actual_user_pname:
                print("Verification Failed - An incorrect user name is displayed on the profile page: " + actual_user_pname )