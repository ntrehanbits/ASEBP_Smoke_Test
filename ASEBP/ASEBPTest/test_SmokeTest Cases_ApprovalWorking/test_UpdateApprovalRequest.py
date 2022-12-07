# Update Approval Request with submit button functionality
import time
import pyperclip
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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
def test_Update_approval_Submit_button(test_login):
    # Click on the Requests tab
    try:
        WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
        WebDriverWait(driver, LONG_TIMEOUT).until_not(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    except TimeoutException:
        pass
    Request_tab = driver.find_element_by_xpath("//li[@title='Requests']/a")
    Request_tab.click()

    # Apply Type Filter as "Approval"
    try:
    #     Type_Filter_Field = driver.find_element_by_xpath("//div[@class='DynamicWidthLayout---dynamic_layout DynamicWidthLayout---align_start']/div[2]")
    #     Type_Filter_Field.click()
    #     # Selecting value from Type field dropdown using Action Chains
    #     action = ActionChains(driver)
    #     action.key_down(Keys.ENTER).perform()
    #     time.sleep(2)
        # Search for the Approval Request Title in Search Field
        Search_Field = driver.find_element_by_xpath("//div[@class='TextInput---input_icon_wrapper TextInput---show_data_icon']/div//input")
        Search_Field.send_keys("Testing Automated Approval Request Title")
        # Click on Search button listed in search request field
        Search_button = driver.find_element_by_xpath("//button[text()='Search']")
        Search_button.click()
        # Apply Status Filter as "Draft"
        Status_Field = driver.find_element_by_xpath("//div[@class='DynamicWidthLayout---dynamic_layout DynamicWidthLayout---align_start']/div[4]")
        Status_Field.click()
        # Selecting value from Type field dropdown using Action Chains
        action = ActionChains(driver)
        action.key_down(Keys.ARROW_DOWN)
        action.key_down(Keys.ARROW_DOWN)
        action.key_down(Keys.ENTER).perform()
        time.sleep(2)
    except:
        print("Filters are not applied on request page correctly")
    # Press outside at screen to get out of drop down widget
    driver.find_element_by_xpath("//div[@class='SiteHeaderLayout---nav_tabs']").click()
    time.sleep(2)

    # Click on the Selected Approval request after applying filters
    try:
        str1 = driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div//a")
        str1.click()
    except:
        print("Unable to click on the selected Approval Request")

    # Click on Update Approval Request button
    try:
        Update_request_button = driver.find_element_by_xpath("//button[text()='Update Request']")
        Update_request_button.click()
        time.sleep(2)
    except:
        print("Update Approval Request button is not clicked")
    # Scroll down and click on Add document link
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # Add new Title for the Approval Request
    try:
        Title = driver.find_element_by_xpath("//div[@class='FieldLayout---field_layout FieldLayout---margin_below_standard FieldLayout---margin_above_none']//div[@class='FieldLayout---input_below']//input")
        Title.clear()
        Title.send_keys("Updated Automated Approval Request Title")
    except:
        print("Unable to add new Title")

    # click on Add document link and add new approver in the list
    try:
        Add_Approver_link = driver.find_element_by_xpath("//a[contains(text(),'Add Approver')]").click()
        # time.sleep(2)
        Approver_2 = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[3]/td[2]//div/input")
        Approver_2.send_keys("Raw user 02")
        time.sleep(2)
        action = ActionChains(driver)
        action.key_down(Keys.ENTER).perform()
    except:
        print("Unable to add new approver in approver list")

    #Clear text from Description field and add new description text
    try:
        Title.click()  # by using tab or action key method clicked on Bold button
        # Click on Editor text area
        action = ActionChains(driver)
        action.send_keys(Keys.TAB * 6).perform()  # Reached on Bold button in description editor
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        action.send_keys(Keys.DELETE).perform()
        TEXT = "Google LLC is an American multinational technology company focusing on search engine technology, online advertising, cloud computing, computer software, quantum computing, e-commerce, artificial intelligence, and consumer electronics."  # Adding Description
        pyperclip.copy(TEXT)  # use to copy the text on clipboard
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # Use to paste the text using action chains
        time.sleep(2)
    except:
        print("Unable to add New Description")

    # Click on Add Document link under Documents Section
    try:
        Add_document = driver.find_element_by_xpath("//a[contains(text(),'Add Document')]")
        Add_document.click()
        time.sleep(1)
    except:
        print("Unable to click on Add document link")

    # Add Title under Documents section
    try:
        Document_title = driver.find_element_by_xpath("//tbody/tr[2]/td[1]/div/input")
        Document_title.send_keys("Doc test update Request title")
        # Click on Link Radio button
        Radio_button_selection = driver.find_element_by_xpath("//tbody/tr[2]/td[2]//label[contains(text(),'Link')]").click()
        time.sleep(2)
        # Add Document/Link text
        Adding_link = driver.find_element_by_xpath("//tbody/tr[2]/td[3]/div/input")
        Adding_link.send_keys("https://asebptest.appiancloud.com/")
        time.sleep(2)
        # Add description for link
        link_description = driver.find_element_by_xpath("//tbody/tr[2]/td[4]/div/textarea")
        link_description.send_keys("Content here, content here', making it look like readable English.Updated Text")
    except:
        print("Unable to add data in Document section in any one field")

    # Click on Submit Button
    try:
        Submit_button = driver.find_element_by_xpath("//button[text()='SUBMIT']")
        Submit_button.click()
    except:
        print("Unable to click on Submit button")