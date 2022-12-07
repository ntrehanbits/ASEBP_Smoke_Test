# Complete My Review Functionality With Final Review marked as "Reviewed" by Reviewer 2
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

# Sign In appian application  by Reviwer 2
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
    Username.send_keys("RAW_USER_01")
    Password = driver.find_element_by_id("pw")
    Password.send_keys("Test123=")
    # Click on SIGN IN button
    Sign_In_Button = driver.find_element_by_xpath("//*[@id='loginForm']/div[4]/div/div[2]/input").click()

@pytest.mark.test
def test_Complete_my_review_button(test_login):
    # Click on Review Tab under My Approval & Review Task
    try:
        Review_tab= driver.find_element_by_xpath("//div[@class='FieldLayout---input_below']/div/p/span[contains(text(),'REVIEW')]")
        Review_tab.click()
        time.sleep(3)
    except:
        print("Unable to click on Review Tab under Approval & Review Task By Reviewer 2")

   # Apply Filter for Search Request field in My Approval & Review Task section
    try:
        Search_Field = driver.find_element_by_xpath("//div[@class='FieldLayout---input_below']/div/input")
        Search_Field.send_keys("Testing Review Automated Title New")
        time.sleep(2)
        # Apply Filter for Owner field in My task section
        Owner_Field =driver.find_element_by_xpath("//input[@class='PickerWidget---picker_input PickerWidget---placeholder']")
        Owner_Field.send_keys("Neha")
        time.sleep(2)
        action = ActionChains(driver)
        action.key_down(Keys.ENTER).perform()
        time.sleep(2)

    except:
       print("Filters are not applied succesfully in My Approval & Review Task section By Reviewer 2")

    # Click on Selected Review request after applied filters
    try:
        Selected_Request = driver.find_element_by_xpath("//tbody/tr/td[2]/div/p//a")
        Selected_Request.click()
        time.sleep(2)
    except:
        print("Unable to click on Selected Review Request after applied Filters By Reviewer 2")

   #Click on Complete My Review button
    try:
        driver.find_element_by_xpath("//button[text()='Complete My Review']").click()
        time.sleep(2)
    except:
       print("Unable to click on Complete My Review button By Reviewer 2")

    #Click on Assessment Editor Field
    try:
        driver.find_element_by_xpath("//div[@data-testid='SectionLayout2-contentContainer']//div[@class='FieldLayout---input_below']//iframe").click()
        time.sleep(3)
        TEXT = " Assessment notes by Reviewer 2 Request is marked as Reviewed"
        pyperclip.copy(TEXT)  # use to copy the text on clipboard
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # Use to paste the text using action chains
        time.sleep(2)
    except:
        print("Unable to add assessment notes By Reviewer 2")

   #Click on the Add document Link
    try:
        Add_document = driver.find_element_by_xpath("//a[contains(text(),'Add Document')]")
        Add_document.click()
        time.sleep(2)
    except:
        print("Unable to click on Document link By Reviewer 2")

    # Add Title,Link & Description under Documents section
    try:
        Document_title = driver.find_element_by_xpath("//tbody[1]/tr[1]/td[1]/div/input")
        Document_title.send_keys("DOC ADDED BY REVIEWER 2 ON COMPLETE MY REVIEW PAGE")
        time.sleep(2)
       # Click on Link Radio button
        Radio_button_selection = driver.find_element_by_xpath("//div[@class='RadioSelect---choice_pair']//label[contains(text(),'Link')]")
        Radio_button_selection.click()
        time.sleep(2)
        # Add Document/Link text
        Adding_link = driver.find_element_by_xpath("//tbody/tr/td[3]/div/input")
        Adding_link.send_keys("https://asebptest.appiancloud.com/")
        # Add description for link
        link_description = driver.find_element_by_xpath("//tbody/tr/td[4]/div/textarea")
        link_description.send_keys("Content here, content here', making it look like readable English.Updated Text")
    except:
        print("Unable to add any one of the field Title,Link & Description under Documents section By Reviewer 2")
   # Scroll down and click on Final Review button
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # Mark Final review as "Approve"
    try:
        Final_review = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---card_choice_template_stacked_bar']")
        Final_review.click()
    except:
        print("Unable to Mark Final Review By Reviewer 2")

   # Click on Submit Button
    try:
        Submit_Button =driver.find_element_by_xpath("//button[text()='Submit']")
        Submit_Button.click()
       # Select yes on confirmation window
        driver.find_element_by_xpath("//button[text()='Yes']").click()
    except:
        print("Unable to click on submit button By Reviewer 2")

