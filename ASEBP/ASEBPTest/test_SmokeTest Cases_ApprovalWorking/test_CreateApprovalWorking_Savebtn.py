# Create Approval Request with Save button Functionality
import pytest as pytest
import time
import pyperclip
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        # wait 10 seconds before looking for element "Create_Approval_Request_button"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='RecordActionWidget---button_layout_inner_wrapper']//button[text()='Create Approval Request']")))
        element.click()
    except:
        print("Unable to click on Create Approval Button")
    else:
        # Adding Title ,Folder & Period  on Create Approval Request Page
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
        # Selecting value from dropdown using Action Chains
        action = ActionChains(driver)
        action.key_down(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ENTER).perform()
    try:
        # Selecting approver on Create Approval Request Page & Press Enter key
        Approver_1 = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[1]//input")
        Approver_1.send_keys("nisha")
        time.sleep(2)
        action = ActionChains(driver)
        action.key_down(Keys.ENTER).perform()
        time.sleep(2)
    except:
        print("Unable to add Approver 1 in the approvers list")
# Click on Add Approver link under workflow section to add more than one approver
    try:
        Add_Approver_link = driver.find_element_by_xpath("//a[contains(text(),'Add Approver')]").click()
        time.sleep(2)
        Approver_2 = driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[2]//input")
        Approver_2.send_keys("Raw")
        time.sleep(2)
        action.key_down(Keys.ENTER).perform()
        time.sleep(2)
    except:
        print("Either unable to  click on add Approver Link or unable to add Approver 2 in the approvers list")
    try:
        # Adding Description on Create Approval Request Page
        Title.click()  # by using tab or action key method clicked on Bold button
        # Click on Editor text area
        action.send_keys(Keys.TAB * 6).perform()  # Reached on Bold button in description editor
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
        TEXT = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like"  # Adding Description
        pyperclip.copy(TEXT)  # use to copy the text on clipboard
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # Use to paste the text using action chains
    except:
        print("Unable to add text in Description section")
        # Scroll down and click on Add document link
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

    #Click on Add Document Link
    try:
        Add_document = driver.find_element_by_xpath("//a[contains(text(),'Add Document')]").click()
        time.sleep(2)
        # Add Title under Documents section
        Document_title = driver.find_element_by_xpath("//tbody//tr/td[1]/div/input")
        Document_title.send_keys("Doc test title")
        # Click on Link Radio button
        Radio_button_selection = driver.find_element_by_xpath("//div[@class='RadioSelect---choice_pair']//label[contains(text(),'Link')]")
        Radio_button_selection.click()
        time.sleep(2)
        # Add Document/Link text
        Adding_link = driver.find_element_by_xpath("//div[@class='EditableGridLayout---scrollable_content']//td[3]//input")
        Adding_link.send_keys("https://rally1.rallydev.com")
        # Add description for link
        link_description = driver.find_element_by_xpath("//td[@class='EditableGridLayout---reducedPadding'][3]/div/textarea")
        link_description.send_keys("Testing description")
    except:
        print("Unable to add data in Document section in any one field")
    try:
        #Click on Save button
        Save_button = driver.find_element_by_xpath("//button[text()='SAVE']")
        Save_button.click()
        time.sleep(2)
    except:
        print("Unable to Click on Save Button")

