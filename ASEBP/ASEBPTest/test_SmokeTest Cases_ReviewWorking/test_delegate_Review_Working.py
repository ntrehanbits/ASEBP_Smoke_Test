# Delegate Review Request to another "Reviewer"
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
    Username.send_keys("nisha.bharti@bitsinglass.com")
    Password = driver.find_element_by_id("pw")
    Password.send_keys("Crochet@786")
    # Click on SIGN IN button
    Sign_In_Button = driver.find_element_by_xpath("//*[@id='loginForm']/div[4]/div/div[2]/input").click()

@pytest.mark.test
def test_Delegate_Review_button(test_login):
    # Click on Review Tab under My Approval & Review Task
    try:
        Review_tab = driver.find_element_by_xpath("//div[@class='FieldLayout---input_below']/div/p/span[contains(text(),'REVIEW')]")
        Review_tab.click()
        time.sleep(3)
    except:
        print("Unable to click on Review Tab under Approval & Review Task")

   # Apply Filter for Search Request field in My task section
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
       print("Filters are not applied succesfully in My Task section")

    # Click on Selected approval request after applied filters
    try:
       Selected_Request = driver.find_element_by_xpath("//tbody/tr/td[2]/div/p//a")
       Selected_Request.click()
       time.sleep(2)
    except:
       print("Unable to click on Selected Review Request after applied Filters")

   #Click on Complete My Approval button
    try:
        driver.find_element_by_xpath("//button[text()='Complete My Review']").click()
        time.sleep(2)
    except:
       print("Unable to click on Complete My Review button")
       # Scroll down and click on Final Review button
       driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # Click on Delegtae button
    try:
        Delegate_Btn=driver.find_element_by_xpath("//div[@class='ButtonLayout2---button_layout ButtonLayout2---align_end ButtonLayout2---margin_below_none ButtonLayout2---margin_above_none']//button")
        Delegate_Btn.click()
        time.sleep(2)
    except:
        print("Unable to click on Delegate button")

    #Click on Find Delegte user Field
    try:
      Find_Delegate= driver.find_element_by_xpath("//div[@class='PickerWidget---picker_value PickerWidget---placeholder_visible']/input")
      Find_Delegate.send_keys("Raw User 03")
      time.sleep(1)
      action = ActionChains(driver)
      action.key_down(Keys.ENTER).perform()
      time.sleep(2)
    except:
       print("Unable to find new delegate user")

    # Click on Submit Button
    try:
        Submit_Button =driver.find_element_by_xpath("//button[text()='Submit']")
        Submit_Button.click()
    except:
        print("Unable to click on submit button")
