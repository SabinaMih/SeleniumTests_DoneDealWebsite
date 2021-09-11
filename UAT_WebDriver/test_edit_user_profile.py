import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import unittest

class test_edit_user_profile(unittest.TestCase):
    chrome_browser = ""
    app_url = ""
    
    def setUp(self):
        self.chrome_webbrowser = webdriver.Chrome("UAT_WebDriver\chromedriver.exe")
        # Go and get the html
        self.app_url = "https://www.donedeal.ie/accounts/classifieds/mydonedeal"

    def tearDown(self):
        # close the web browser
        self.chrome_webbrowser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.chrome_webbrowser.quit()
        
    def test_edit_user_profile_Succesful_inChrome(self):
        # launch the chrome browser and open the application url
        self.chrome_webbrowser.get(self.app_url)

        # maximize the browser window
        self.chrome_webbrowser.maximize_window()

        # close and accept cookies policy 
        self.chrome_webbrowser.implicitly_wait(4)
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').is_displayed:
            cookie_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]')
            self.chrome_webbrowser.execute_script("arguments[0].click()", cookie_btn)


        #log in check if name of input fields are displayed
        self.chrome_webbrowser.implicitly_wait(4)

        user_email = self.chrome_webbrowser.find_element_by_id('email')
        user_password = self.chrome_webbrowser.find_element_by_id('password') 
        if user_email.is_displayed() and user_password.is_displayed():
            # enter user email
            user_email.send_keys("sabinam@gmail.com")
            user_password.send_keys("donedeaL2020" + Keys.RETURN)
        
        # store the expected title of the webpage.
        expected_title = "DoneDeal.ie - Ireland's biggest classifieds site" 
        # actual title on Web Page
        actual_title = self.chrome_webbrowser.title
    
        # verify title and display the actual title
        if expected_title != actual_title:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_title )
            # assert (stop the test)
            assert expected_title in actual_title
        
        # check  heading "My profile"
        expected_heading = "My Profile" 
        # actual title on Web Page
        actual_heading = self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[1]/div[1]/span[2]').text
    
        # verify title and display the actual title
        if expected_heading != actual_heading:
            print("Verification Failed - An incorrect heading is displayed on the web page: " + actual_heading )
            # assert (stop the test)
            assert expected_heading in actual_heading
        
        # check  user name "Sabina"
        expected_name = "Sabina" 
        # actual title on Web Page
        actual_name = self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[1]/div/div/span[2]').text
    
        # verify title and display the actual title
        if expected_name != actual_name:
            print("Verification Failed - An incorrect heading is displayed on the web page: " + actual_name )
            # assert (stop the test)
            assert expected_name in actual_name
        
        # Change user name
        user_new_name = self.chrome_webbrowser.find_element_by_xpath('//*[@id="name"]')
        user_new_name.clear()
        user_new_name.send_keys("Lidia")
        # Change County
        user_county = Select(self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[3]/div[2]/div/select'))
        user_county.select_by_visible_text('Kildare')
        # Change nearest town
        user_county = Select(self.chrome_webbrowser.find_element_by_xpath('//*[@id="town"]'))
        user_county.select_by_visible_text('Naas')

        # check if the email field is dissabled 
        if not self.chrome_webbrowser.find_element_by_xpath('//*[@id="email"]').click():
            print("This email option is disabled")
        
        # check if the phone field is dissabled 
        if not self.chrome_webbrowser.find_element_by_xpath('//*[@id="telephone"]').click():
            print("This phone option is disabled")
        
        # check if the email verified text is present 
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[6]/div[1]/span[1]').is_displayed:
            print("The email verified text is displayed")

        # check if the phone verified text is present 
        if self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[7]/div[1]/span').is_displayed:
            print("The phone verified text is displayed")
        
        # click on the change password link
        change_password = self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[8]/div[2]/span[2]/a').click()
        # Current password
        current_password = self.chrome_webbrowser.find_element_by_id('password')
        current_password.send_keys("donedeaL2020")
        # New password
        new_password = self.chrome_webbrowser.find_element_by_id('confirmPassword')
        new_password.send_keys("donedeAL2020")
        # Confirm password
        confirm_password = self.chrome_webbrowser.find_element_by_id('confirmPassword2')
        confirm_password.send_keys("donedeAL2020")
        # Save button for changing the password
        save_btn = self.chrome_webbrowser.find_element_by_xpath('//*[@id="pwdForm"]/div[4]/button').click()
         # Save button for saving the changes
        save_btn_main = self.chrome_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[15]/div[2]/button').click()
        #click on the user menu and log out
        self.chrome_webbrowser.implicitly_wait(6)
        profile_menu = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div/div/div/div/a[3]/span[2]').click()
        logout = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div/div/div/div/div[2]/ul/li[8]/a').click()
        
        

        #log in again with new password 
        self.chrome_webbrowser.implicitly_wait(6)
        if self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/div[1]/a[1]').is_displayed:
            login = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/div[1]/a[1]')
            self.chrome_webbrowser.execute_script("arguments[0].click()", login)
            
            user_email1 = self.chrome_webbrowser.find_element_by_xpath('//*[@id="email"]')
            user_email1.send_keys("sabinam@gmail.com")
            user_password1 = self.chrome_webbrowser.find_element_by_xpath('//*[@id="password"]')    
            user_password1.send_keys("donedeAL2020" + Keys.RETURN)
            
            # check if the new user name "Lidia" is displayed
            self.chrome_webbrowser.implicitly_wait(4)
            expected_name = "Lidia" 
            # actual title on Web Page
            actual_name = self.chrome_webbrowser.find_element_by_xpath('/html/body/header/div/div/div/div/a[3]/span[2]').text
        
            # verify title and display the actual title
            if expected_name != actual_name:
                print("Verification Failed - An incorrect name is displayed: " + actual_name)
                # assert (stop the test)
                assert expected_name in actual_name
        else:
            print("Log in link is not found")

class test_edit_user_profile_in_FireFox(unittest.TestCase):
    chrome_browser = ""
    app_url = ""
    
    def setUp(self):
        self.chrome_webbrowser = webdriver.Firefox("UAT_WebDriver\geckodriver.exe")
        # Go and get the html
        self.app_url = "https://www.donedeal.ie/accounts/classifieds/mydonedeal"

    def tearDown(self):
        # close the web browser
        self.firefox_webbrowser.close()
        print("Test script executed successfully.")
        time.sleep(4)
        self.firefox_webbrowser.quit()
        
    def test_edit_user_profile_Succesful_in_FireFox(self):
        # launch the chrome browser and open the application url
        self.firefox_webbrowser.get(self.app_url)

        # maximize the browser window
        self.firefox_webbrowser.maximize_window()

        # close and accept cookies policy 
        self.firefox_webbrowser.implicitly_wait(4)
        if self.firefox_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').is_displayed:
            cookie_btn = self.firefox_webbrowser.find_element_by_xpath('//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]')
            self.firefox_webbrowser.execute_script("arguments[0].click()", cookie_btn)


        #log in check if name of input fields are displayed
        self.firefox_webbrowser.implicitly_wait(4)

        user_email = self.firefox_webbrowser.find_element_by_id('email')
        user_password = self.firefox_webbrowser.find_element_by_id('password') 
        if user_email.is_displayed() and user_password.is_displayed():
            # enter user email
            user_email.send_keys("sabinam@gmail.com")
            user_password.send_keys("donedeaL2020" + Keys.RETURN)
        
        # store the expected title of the webpage.
        expected_title = "DoneDeal.ie - Ireland's biggest classifieds site" 
        # actual title on Web Page
        actual_title = self.firefox_webbrowser.title
    
        # verify title and display the actual title
        if expected_title != actual_title:
            print("Verification Failed - An incorrect title is displayed on the web page: " + actual_title )
            # assert (stop the test)
            assert expected_title in actual_title
        
        # check  heading "My profile"
        expected_heading = "My Profile" 
        # actual title on Web Page
        actual_heading = self.firefox_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[1]/div[1]/span[2]').text
    
        # verify title and display the actual title
        if expected_heading != actual_heading:
            print("Verification Failed - An incorrect heading is displayed on the web page: " + actual_heading )
            
        # check  user name "Sabina"
        expected_name = "Sabina" 
        # actual title on Web Page
        actual_name = self.firefox_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[1]/div/div/span[2]').text
    
        # verify title and display the actual title
        if expected_name != actual_name:
            print("Verification Failed - An incorrect heading is displayed on the web page: " + actual_name )
            
        # Change user name
        user_new_name = self.firefox_webbrowser.find_element_by_xpath('//*[@id="name"]')
        user_new_name.clear()
        user_new_name.send_keys("Lidia")
        # Change County
        user_county = Select(self.firefox_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[3]/div[2]/div/select'))
        user_county.select_by_visible_text('Kildare')
        # Change nearest town
        user_county = Select(self.firefox_webbrowser.find_element_by_xpath('//*[@id="town"]'))
        user_county.select_by_visible_text('Naas')

        # check if the email field is dissabled 
        if not self.firefox_webbrowser.find_element_by_xpath('//*[@id="email"]').click():
            print("This email option is disabled")
        
        # check if the phone field is dissabled 
        if not self.firefox_webbrowser.find_element_by_xpath('//*[@id="telephone"]').click():
            print("This phone option is disabled")
        
        # check if the email verified text is present 
        if self.firefox_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[6]/div[1]/span[1]').is_displayed:
            print("The email verified text is displayed")

        # check if the phone verified text is present 
        if self.firefox_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[7]/div[1]/span').is_displayed:
            print("The phone verified text is displayed")
        
        # click on the change password link
        change_password = self.firefox_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[8]/div[2]/span[2]/a').click()
        # Current password
        current_password = self.firefox_webbrowser.find_element_by_id('password')
        current_password.send_keys("donedeaL2020")
        # New password
        new_password = self.firefox_webbrowser.find_element_by_id('confirmPassword')
        new_password.send_keys("donedeAL2020")
        # Confirm password
        confirm_password = self.firefox_webbrowser.find_element_by_id('confirmPassword2')
        confirm_password.send_keys("donedeAL2020")
        # Save button for changing the password
        save_btn = self.firefox_webbrowser.find_element_by_xpath('//*[@id="pwdForm"]/div[4]/button').click()
         # Save button for saving the changes
        save_btn_main = self.firefox_webbrowser.find_element_by_xpath('//*[@id="dashboardContent"]/div[3]/div/div/div[2]/form/ul/li[15]/div[2]/button').click()
        #click on the user menu and log out
        self.firefox_webbrowser.implicitly_wait(6)
        profile_menu = self.firefox_webbrowser.find_element_by_xpath('/html/body/header/div/div/div/div/a[3]/span[2]').click()
        logout = self.firefox_webbrowser.find_element_by_xpath('/html/body/header/div/div/div/div/div[2]/ul/li[8]/a').click()
        
        

        #log in again with new password 
        self.firefox_webbrowser.implicitly_wait(6)
        if self.firefox_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/div[1]/a[1]').is_displayed:
            login = self.firefox_webbrowser.find_element_by_xpath('/html/body/header/div[1]/div/div/div/div[1]/a[1]')
            self.firefox_webbrowser.execute_script("arguments[0].click()", login)
            
            user_email1 = self.firefox_webbrowser.find_element_by_xpath('//*[@id="email"]')
            user_email1.send_keys("sabinam@gmail.com")
            user_password1 = self.firefox_webbrowser.find_element_by_xpath('//*[@id="password"]')    
            user_password1.send_keys("donedeAL2020" + Keys.RETURN)
            
            # check if the new user name "Lidia" is displayed
            self.firefox_webbrowser.implicitly_wait(4)
            expected_name = "Lidia" 
            # actual title on Web Page
            actual_name = self.firefox_webbrowser.find_element_by_xpath('/html/body/header/div/div/div/div/a[3]/span[2]').text
        
            # verify title and display the actual title
            if expected_name != actual_name:
                print("Verification Failed - An incorrect name is displayed: " + actual_name)
        else:
            print("Log in link is not found")