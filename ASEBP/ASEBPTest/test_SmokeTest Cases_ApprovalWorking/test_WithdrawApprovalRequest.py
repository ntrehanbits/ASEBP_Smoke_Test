# Withdraw Approval Request Functionality
import time
import pyperclip
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
SHORT_TIMEOUT = 5
LONG_TIMEOUT = 400
LOADING_ELEMENT_XPATH = "//div[@id='appian-working-indicator-hidden']"

@pytest.fixture
def test_login():
    global driver
    # Initiating Chrome driver
    driver = webdriver.Chrome("C:/Users/Neha/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://asebptest.appiancloud.com/suite/sites/review-and-approval-workflow-users")
    driver.implicitly_wait(5)
    # Login with username & password
    Username = driver.find_element_by_id("un")
    Username.send_keys("neha.trehan@bitsinglass.com")
    Password = driver.find_element_by_id("pw")
    Password.send_keys("Crochet@786")
    # Click on SIGN IN button
    Sign_In_Button = driver.find_element_by_xpath("//*[@id='loginForm']/div[4]/div/div[2]/input").click()

@pytest.mark.test
def test_Withdraw_approval_Submit_button(test_login):
    # Click on the Requests tab
    Request_tab = driver.find_element_by_xpath("//li[@title='Requests']/a").click()
    try:
        WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
        WebDriverWait(driver, LONG_TIMEOUT).until_not(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    except TimeoutException:
        pass

    # Search for the Approval Request Title in Search Field and apply filter as submitted
    try:
        Search_Field = driver.find_element_by_xpath("//div[@class='TextInput---input_icon_wrapper TextInput---show_data_icon']/div//input")
        Search_Field.send_keys("Testing Automated Approval Request Title")
        time.sleep(2)
        # Click on Search button
        Search_button = driver.find_element_by_xpath("//button[text()='Search']").click()
        time.sleep(2)
        # Apply Status Filter as "Submitted"
        Status_Field = driver.find_element_by_xpath("//div[@class='DynamicWidthLayout---dynamic_layout DynamicWidthLayout---align_start']/div[4]")
        Status_Field.click()
        # Selecting value from Type field dropdown using Action Chains
        action = ActionChains(driver)
        action.key_down(Keys.ARROW_DOWN)
        action.key_down(Keys.ARROW_DOWN)
        action.key_down(Keys.ARROW_DOWN)
        action.key_down(Keys.ARROW_DOWN)
        action.key_down(Keys.ARROW_DOWN)
        action.key_down(Keys.ENTER).perform()
        time.sleep(2)
    except:
        print("Filters are not applied on request page correctly")
    # Press outside at screen to get out of drop down widget
    driver.find_element_by_xpath("//div[@class='SiteHeaderLayout---nav_tabs']").click()
    time.sleep(2)

    # Click on the Approval request
    try:
        str1 = driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div//a")
        str1.click()
    except:
        print("Unable to click on the selected request")

    #Click on Withdraw Request button
    try:
        Withdraw_Request_button= driver.find_element_by_xpath("//button[text()='Withdraw Request']")
        Withdraw_Request_button.click()
        time.sleep(3)
    except:
        print("Unable to click on Withdraw Request button")

    #Click on Editor text area
    try:
        action = ActionChains(driver)
        action.send_keys(Keys.TAB * 6).perform()  # Reached on Bold button in description editor
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
        TEXT = " Reason for Withdrawal"
        pyperclip.copy(TEXT) # use to copy the text on clipboard
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # Use to paste the text using action chains
        time.sleep(2)
    except:
        print("Unable to add reasons of withdrawal")

    #Click on Submit Button and select Yes in confirmation window
    try:
        Submit_button = driver.find_element_by_xpath("//div[@class='ColumnArrayLayout---column_layout ColumnArrayLayout---standard_spacing']//div[2]//button").click()
        #get prompt message on click of submit button
        Str2= driver.find_element_by_xpath("//p[text()='This will withdraw your request, are you sure you want to continue?']")
        print(Str2)
        #Click on Yes in Confirmation window to withdraw request
        btn= driver.find_element_by_xpath("//button[text()='Yes']")
        btn.click()
    except:
        print("Unable to click on submit button")
