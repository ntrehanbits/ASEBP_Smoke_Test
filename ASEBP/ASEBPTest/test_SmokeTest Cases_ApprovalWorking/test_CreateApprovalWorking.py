# Create Approval Request with Save button Functionality
import time
from telnetlib import EC
import pyperclip
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
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
def test_Create_approval_Save_button(test_login):
    try:
        # Click on Create Approval Request button
        Create_Approval_Request_button = driver.find_element_by_xpath("//div[@class='RecordActionWidget---button_layout_inner_wrapper']//button[text()='Create Approval Request']")
        Create_Approval_Request_button.click()
        time.sleep(5)
        # Adding Title on Create Approval Request Page
        Title = driver.find_element_by_xpath("//div[@class='FieldLayout---field_layout FieldLayout---margin_below_standard FieldLayout---margin_above_none']//div[@class='FieldLayout---input_below']//input")
        Title.send_keys("Testing Automated Approval Request Title")
        # Selecting Folder on Create Approval Request Page
        Folder_field = driver.find_element_by_xpath("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder DropdownWidget---inSideBySideItem']")
        Folder_field.click()
        # Selecting value from dropdown using Action Chains
        action = ActionChains(driver)
        action.key_down(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ENTER).perform()
        # Selecting Period on Create Approval Request Page
        Period_field = driver.find_element_by_xpath("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder DropdownWidget---inSideBySideItem']")
        Period_field.click()
        # Selecting value from dropdown
        action = ActionChains(driver)
        action.key_down(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ENTER).perform()
        # Selecting approver on Create Approval Request Page & Press Enter key
        Approver_1 = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[1]//input")
        Approver_1.send_keys("nisha")
        time.sleep(2)
        action.key_down(Keys.ENTER).perform()
        time.sleep(1)
        # Click on Add Approver link under workflow section to add more than one approver
        Add_Approver_link = driver.find_element_by_xpath("//a[contains(text(),'Add Approver')]").click()
        time.sleep(2)
        Approver_2 = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[2]//input")
        Approver_2.send_keys("jon")
        time.sleep(2)
        action.key_down(Keys.ENTER).perform()
        time.sleep(3)
        # Adding Description on Create Approval Request Page
        Title.click()  # by using tab or action key method clicked on Bold button
        time.sleep(2)
        action.send_keys(Keys.TAB * 6).perform()  # Reached on Bold button in description editor
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
        TEXT = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like"  # Adding Description
        pyperclip.copy(TEXT)  # use to copy the text on clipboard
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(
            Keys.CONTROL).perform()  # Use to paste the text using action chains
        # Scroll down and click on Add document link
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        Add_document = driver.find_element_by_xpath("//a[contains(text(),'Add Document')]").click()
        time.sleep(2)
        # Add Title under Documents section
        Document_title = driver.find_element_by_xpath("//tbody//tr/td[1]/div/input").send_keys("Doc test title")
        # Click on Link Radio button
        Radio_button_selection = driver.find_element_by_xpath("//div[@class='RadioSelect---choice_pair']//label[contains(text(),'Link')]").click()
        time.sleep(3)
        # Add Document/Link text
        Adding_link = driver.find_element_by_xpath("//div[@class='EditableGridLayout---scrollable_content']//td[3]//input")
        Adding_link.send_keys("https://rally1.rallydev.com")
        time.sleep(3)
        # Add description for link
        link_description = driver.find_element_by_xpath("//td[@class='EditableGridLayout---reducedPadding'][3]/div/textarea")
        link_description.send_keys("Testing description")
        time.sleep(2)
        # Click on Save Button
        Save_button = driver.find_element_by_xpath("//button[text()='SAVE']").click()
        time.sleep(2)
    except Exception:
        pass

@pytest.mark.test
def test_Create_approval_Submit_button(test_login):
    # Click on the Requests tab
    try:
        WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
        WebDriverWait(driver, LONG_TIMEOUT).until_not(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    except TimeoutException:
        pass
    Request_tab = driver.find_element_by_xpath("//li[@title='Requests']/a").click()
    # Apply Type Filter as "Approval"
    Type_Filter_Field = driver.find_element_by_xpath("//div[@class='DynamicWidthLayout---dynamic_layout DynamicWidthLayout---align_start']/div[2]")
    Type_Filter_Field.click()
    # Selecting value from Type field dropdown using Action Chains
    action = ActionChains(driver)
    action.key_down(Keys.ENTER).perform()
    time.sleep(2)
    # Search for the Approval Request Title in Search Field
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
    action.key_down(Keys.ENTER).perform()
    time.sleep(2)
    # Press outside at screen to get out of drop down widget
    driver.find_element_by_xpath("//div[@class='SiteHeaderLayout---nav_tabs']").click()
    time.sleep(2)
    # Click on the Approval request
    str1 = driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div//a")
    str1.click()
    time.sleep(3)
    # Click on Update Review Request button
    Update_request_button = driver.find_element_by_xpath("//button[text()='Update Request']").click()
    time.sleep(2)
    # Scroll down and click on Add document link
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    # Click on Add Document Link
    Add_document = driver.find_element_by_xpath("//a[contains(text(),'Add Document')]").click()
    time.sleep(3)
    # Add Title under Documents section
    Document_title = driver.find_element_by_xpath("//tbody/tr[2]/td[1]/div/input")
    Document_title.send_keys("Doc test update Request title")
    # Click on Link Radio button
    Radio_button_selection = driver.find_element_by_xpath("//tbody/tr[2]/td[2]//label[contains(text(),'Link')]")
    Radio_button_selection.click()
    time.sleep(3)
    # Add Document/Link text
    Adding_link = driver.find_element_by_xpath("//tbody/tr[2]/td[3]/div/input")
    Adding_link.send_keys("https://asebptest.appiancloud.com/")
    time.sleep(3)
    # Add description for link
    link_description = driver.find_element_by_xpath("//tbody/tr[2]/td[4]/div/textarea")
    link_description.send_keys("Content here, content here', making it look like readable English.Updated Text")
    time.sleep(2)
    # Click on Submit Button
    Submit_button = driver.find_element_by_xpath("//button[text()='SUBMIT']").click()

@pytest.mark.test
def test_Create_approval_Submitt_button(test_login):
    Create_Approval_Request_button = driver.find_element_by_xpath("//div[@class='RecordActionWidget---button_layout_inner_wrapper']//button[text()='Create Approval Request']")
    Create_Approval_Request_button.click()
    time.sleep(5)
    # Adding Title on Create Approval Request Page
    Title = driver.find_element_by_xpath("//div[@class='FieldLayout---field_layout FieldLayout---margin_below_standard FieldLayout---margin_above_none']//div[@class='FieldLayout---input_below']//input")
    Title.send_keys("Testing Automated Approval Request Title")
    # Selecting Folder on Create Approval Request Page
    Folder_field = driver.find_element_by_xpath("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder DropdownWidget---inSideBySideItem']")
    Folder_field.click()
    # Selecting value from dropdown using Action Chains
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).perform()
    # Selecting Period on Create Approval Request Page
    Period_field = driver.find_element_by_xpath("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder DropdownWidget---inSideBySideItem']")
    Period_field.click()
    # Selecting value from dropdown
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).perform()
    # Selecting approver on Create Approval Request Page & Press Enter key
    Approver_1 = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[1]//input")
    Approver_1.send_keys("nisha")
    time.sleep(2)
    action.key_down(Keys.ENTER).perform()
    time.sleep(2)
    # Click on Add Approver link under workflow section to add more than one approver
    Add_Approver_link = driver.find_element_by_xpath("//a[contains(text(),'Add Approver')]").click()
    time.sleep(2)
    Approver_2 = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[2]//input")
    Approver_2.send_keys("jon")
    time.sleep(3)
    action.key_down(Keys.ENTER).perform()
    time.sleep(3)
    # Adding Description on Create Approval Request Page
    Title.click()  # by using tab or action key method clicked on Bold button
    time.sleep(2)
    action.send_keys(Keys.TAB * 6).perform()  # Reached on Bold button in description editor
    time.sleep(2)
    action.send_keys(Keys.ENTER).perform()
    TEXT = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like"  # Adding Description
    pyperclip.copy(TEXT)  # use to copy the text on clipboard
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(
        Keys.CONTROL).perform()  # Use to paste the text using action chains
    # Scroll down and click on Add document link
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    Add_document = driver.find_element_by_xpath("//a[contains(text(),'Add Document')]").click()
    time.sleep(2)
    # Add Title under Documents section
    Document_title = driver.find_element_by_xpath("//tbody//tr/td[1]/div/input")
    Document_title.send_keys("Doc test title")
    # Click on Link Radio button
    Radio_button_selection = driver.find_element_by_xpath("//div[@class='RadioSelect---choice_pair']//label[contains(text(),'Link')]").click()
    time.sleep(3)
    # Add Document/Link text
    Adding_link = driver.find_element_by_xpath("//div[@class='EditableGridLayout---scrollable_content']//td[3]//input")
    Adding_link.send_keys("https://rally1.rallydev.com")
    time.sleep(3)
    # Add description for link
    link_description = driver.find_element_by_xpath("//td[@class='EditableGridLayout---reducedPadding'][3]/div/textarea")
    link_description.send_keys("Testing description")
    time.sleep(2)
    # Click on Submit Button
    Save_button = driver.find_element_by_xpath("//button[text()='SUBMIT']").click()
    time.sleep(2)
