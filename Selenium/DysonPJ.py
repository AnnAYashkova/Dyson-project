
import time
import random
from encodings import cp775 as driver
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import HtmlTestRunner
from allure_unittest import Run
import unittest
import HtmlTestRunner

import allure_unittest
import subprocess


class DysonWebsite(unittest.TestCase):
    # Set up Chrome and maximize window

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()

        # Check that you are on correct page

    def test_1_Sign_in(self):
        driver = self.driver
        print("Test 1 Sign in ")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-c96cd862-339c2642"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-c96cd862-339c2642"]').click()

        print("Sign in form appeared")

        wait.until(EC.visibility_of_element_located((By.ID, "login-email")))
        driver.find_element(By.ID, "login-email").send_keys("postfortestrail@gmail.com")

        wait.until(EC.visibility_of_element_located((By.ID, "password")))
        driver.find_element(By.ID, "password").send_keys("TestPass00")

        wait.until(EC.element_to_be_clickable((By.ID, "my-dyson-login__login-button")))
        driver.find_element(By.ID, "my-dyson-login__login-button").click()

        # Check that log in was successfully done

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@data-di-id="di-id-2193ae77-9cd850b4"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-di-id="di-id-19ed60e3-1167de31"]'))).click()

    def test_2_Main_menu(self):
        driver = self.driver
        print("Test 2 Validate that 'Main menu' links lead to the right pages and have proper title)")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        # Check Main menu

        print("Validate that 'Main menu' links lead to the right pages and have proper title)")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-analytics-nav-name="dyson renewed"]')))
        driver.find_element(By.XPATH, '//a[@data-analytics-nav-name="dyson renewed"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="js-rich-content-main-container "]')))

        # Check "Dyson Renewed"

        try:
            assert "Dyson Outlet. Expertly refurbished Dyson technology." in driver.title
            print("Dyson Renewed, Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/outlet" in driver.current_url
            print("Dyson Renewed,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Find a store"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-analytics-nav-name="find a store"]')))
        driver.find_element(By.XPATH, '//a[@data-analytics-nav-name="find a store"]').click()

        try:
            assert "Dyson Stores | Dyson Stores" in driver.title
            print("Find a store, Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/demo-stores" in driver.current_url
            print("Find a store ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "For business"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-analytics-nav-name="for business"]')))
        driver.find_element(By.XPATH, '//a[@data-analytics-nav-name="for business"]').click()

        try:
            assert "Commercial fixtures for business environments | Dyson" in driver.title
            print("For business, Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/commercial/products" in driver.current_url
            print("For business ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Register machine"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-analytics-nav-name="register machine"]')))
        driver.find_element(By.XPATH, '//a[@data-analytics-nav-name="register machine"]').click()

        try:
            assert "Dyson Product Registration | Dyson" in driver.title
            print("Register machine, Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/registration" in driver.current_url
            print("Register machine ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Contact us"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-analytics-nav-name="contact us"]')))
        driver.find_element(By.XPATH, '//a[@data-analytics-nav-name="contact us"]').click()

        try:
            assert "Contact us | Dyson" in driver.title
            print("Contact us , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/support/contact-us" in driver.current_url
            print("Contact us ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Sign in Join"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-c96cd862-339c2642"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-c96cd862-339c2642"]').click()

        try:
            assert "My Dyson | Dyson" in driver.title
            print("Sign in Join , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/your-dyson" in driver.current_url
            print("Sign in Join ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

    def test_3_Shop_menu(self):
        driver = self.driver
        print("Test 5 Validate that 'Shop menu' links lead to the right pages and have proper title)")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        # Check "Deals"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-26df8411-7580030e"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-26df8411-7580030e"]').click()

        try:
            assert "Dyson Deals & Offers | Dyson" in driver.title
            print("Deals , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/deals" in driver.current_url
            print("Deals  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Floor care"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-c0aa933c-3d98d6d5"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-c0aa933c-3d98d6d5"]').click()

        try:
            assert "Vacuum Cleaners | Dyson" in driver.title
            print("Floorcare , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/vacuum-cleaners" in driver.current_url
            print("Floorcare  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Hair care"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-d804deaa-12de202e"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-d804deaa-12de202e"]').click()

        try:
            assert "Dyson hair care | Dyson" in driver.title
            print("Hair care , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/hair-care" in driver.current_url
            print("Hair care  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Air treatment"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-1f95e17b-8c45d4bf"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-1f95e17b-8c45d4bf"]').click()

        try:
            assert "Air Treatment, Air Purifiers, Heaters, Fans, Humidifiers, Purifier Filters | Dyson" in driver.title
            print("Air treatment , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/air-treatment" in driver.current_url
            print("Air treatment  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Headphones"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-d804deaa-f12f9106"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-d804deaa-f12f9106"]').click()

        try:
            assert "Headphones" in driver.title
            print("Headphones , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/headphones" in driver.current_url
            print("Headphones  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check Lighting

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-69f00eb-baf37625"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-69f00eb-baf37625"]').click()

        try:
            assert "Modern & Contemporary LED Lighting | Dyson" in driver.title
            print("Lighting , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/lighting" in driver.current_url
            print("Lighting  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Support"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-69f00eb-f5965cbb"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-69f00eb-f5965cbb"]').click()

        try:
            assert "Support | Customer Service | Dyson" in driver.title
            print("Support , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/support" in driver.current_url
            print("Support  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        # Check "Gifts"

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-26df8411-14277a88"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-26df8411-14277a88"]').click()

        try:
            assert "Gift guide" in driver.title
            print("Gift guide , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/dyson-live" in driver.current_url
            print("Dyson Live  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

    def test_4_Home_page_Dyson(self):
        driver = self.driver
        print("Test 4 Validate that Home button 'Dyson' links lead to the right pages and have proper title)")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-b3dea005-ccb5704c"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-b3dea005-ccb5704c"]').click()

        try:
            assert (
                    "Dyson vacuum cleaners, hair dryers and stylers, fans, humidifiers, hand dryers and lighting | Dyson"
                    in driver.title)
            print("Home button 'Dyson'  , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/en" in driver.current_url
            print("Home button 'Dyson'  ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

    def test_5_ShopMenu_button(self):
        driver = self.driver
        print("Test 5 Validate that buttom 'Shop menu' links lead to the right pages and have proper title)")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-analytics-action-name="cta~shop now"]')))
        driver.find_element(By.XPATH, '//a[@data-analytics-action-name="cta~shop now"]').click()

        try:
            assert ("Dyson Deals & Offers | Dyson" in driver.title)
            print("Button 'Shop now'  , Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        try:
            assert "https://www.dyson.com/deals" in driver.current_url
            print("Button 'Shop now' ,URL is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

    def test_6_Search_menu(self):
        driver = self.driver
        print("Test 5 Add item from 'Search menu' to basket")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        # Go to the main page

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-di-id="di-id-fe243b83-bf6925d5"]')))
        driver.find_element(By.XPATH, '//button[@data-di-id="di-id-fe243b83-bf6925d5"]').click()

        # Fill in input proper item

        wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="searchText"]')))
        driver.find_element(By.XPATH, '//input[@name="searchText"]').send_keys("airwrap")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-di-id="di-id-349a4ef1-92ee39ef"]')))
        driver.find_element(By.XPATH, '//button[@data-di-id="di-id-349a4ef1-92ee39ef"]').click()

        # Check that you on correct page

        try:
            assert ("Search Results | Dyson" in driver.title)
            print("Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-3bdc42da-e0d693c9"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-3bdc42da-e0d693c9"]').click()

        # Check that you on correct page

        try:
            assert ("Special edition Dyson Airwrap™ multi-styler and dryer Curly+Coily (Strawberry Bronze/Blush Pink)"
                    in driver.title)
            print("Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-di-id="di-id-a2e2a726-b898c0bf"]')))
        driver.find_element(By.XPATH, '//button[@data-di-id="di-id-a2e2a726-b898c0bf"]').click()

        # Check that you on correct page

        try:
            assert ("Error Special edition Dyson Airwrap™ multi-styler and dryer Curly+Coily (Strawberry Bronze/Blush "
                    "Pink)" in driver.title)
            print("Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-di-id="di-id-747e5ab9-5894411b"]')))
        driver.find_element(By.XPATH, '//button[@data-di-id="di-id-747e5ab9-5894411b"]').click()

        # Check item in basket

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//h2[@class="basket-amazon-button__checkout-text basket-text"]')))

        try:
            assert ("Basket | Dyson" in driver.title)
            print("Title is correct", driver.title)
        except AssertionError:
            print("Error", driver.title)

        print("Item in the basket!")

        # Delete item

        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-di-id="di-id-88060844-1167de31"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-88060844-1167de31"]').click()

        try:
            assert ("Dyson vacuum cleaners, hair dryers and stylers, fans, humidifiers, hand dryers and lighting | "
                    "Dyson"
                    in driver.title)
            print("Home button 'Dyson'  , Title is correct", driver.title)
        except AssertionError:

            print("Error", driver.title)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-eee8ef95-558f6874"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-eee8ef95-558f6874"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-2cddc2c3-7dad5fb8"]')))

        try:
            assert ("https://www.dyson.com/basket" in driver.current_url)
            print("Url is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//a[@class="basket-item__remove-link js-basket-item-remove"]'))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@data-di-id="di-id-af2900f3-c0e04a4b"]')))
        driver.find_element(By.XPATH, '//button[@class="button button--interactive basket-item__remove-confirm '
                                      'js-basket-item-remove-confirm col-xs-6"]').click()

        print("Your item removed!")

        driver.back()

    def test_7_Add_item_ShopMenu(self):
        driver = self.driver
        print("Test 6 Add item to Basket from 'Shop menu'")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-ed2366c-e52b97b2"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-ed2366c-e52b97b2"]').click()

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)

        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-di-id="di-id-6e456b58-c49d22f"]'))).click()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-di-id="di-id-b2fa8df7-f709180d"]'))).click()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-di-id="di-id-747e5ab9-5894411b"]'))).click()

        try:
            assert ("https://www.dyson.com/basket" in driver.current_url)
            print("Url is correct", driver.current_url)
        except AssertionError:
            print("Error", driver.current_url)

        print("Item in the basket")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-di-id="di-id-2fec8bd2-4d3f472c"]')))
        driver.find_element(By.XPATH, '//a[@data-di-id="di-id-2fec8bd2-4d3f472c"]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@data-di-id="di-id-af2900f3-c0e04a4b"]')))
        driver.find_element(By.XPATH, '//button[@data-di-id="di-id-af2900f3-c0e04a4b"]').click()

        print("Item removed !")

    def test_8_ChatMenu_Switch_Iframe(self):
        driver = self.driver
        print("Test 7 Send  messages from Chat menu")
        driver.get('https://www.dyson.com/en')
        wait = WebDriverWait(driver, 10, 1)

        wait.until(EC.element_to_be_clickable((By.XPATH, '//button['
                                                         '@data-di-id="#embeddedMessagingConversationButton"]')))
        driver.find_element(By.XPATH, '//button[@data-di-id="#embeddedMessagingConversationButton"]').click()

        # Fill a message in textarea

        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="Chat with an Agent"]'))

        wait.until(EC.visibility_of_element_located((By.XPATH, '//textarea[@aria-label="Chat message"]')))

        # Type a message

        driver.find_element(By.XPATH, '//textarea[@aria-label="Chat message"]').send_keys("Hi!")

        # Click on button and send

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@title="Send message"]')))
        driver.find_element(By.XPATH, '//button[@title="Send message"]').click()

        print("Message was sent!")

        # Click on Help me buy

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@title="Help me buy"]')))
        driver.find_element(By.XPATH, '//button[@title="Help me buy"]').click()

        # Click on Hair care

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@title="Hair care"]')))
        driver.find_element(By.XPATH, '//button[@title="Hair care"]').click()

        # Click on End chat

        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@title="End Chat"]')))
        driver.find_element(By.XPATH, '//button[@title="End Chat"]').click()

        print("Chat is closed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #Standard unitest flow
    unittest.main()
    #HTML reports
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))
    #Allure reports
    #dysonSuite = unittest.defaultTestLoader.loadTestsFromTestCase(DysonWebsite)
    #Run('AllureReports', dysonSuite, clean=True)
    #subprocess.run(["allure", "generate", "./AllureReports"], shell=True)
    #subprocess.run(["allure", "open", "allure-report"], shell=True)
