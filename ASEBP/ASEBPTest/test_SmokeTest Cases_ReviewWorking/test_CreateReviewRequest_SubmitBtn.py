# Create Review Request with Submit button Functionality
import time
import pyperclip as pyperclip
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

#Initiating Chrome driver
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
def test_Create_Review_Save_button(test_login):
    try:
        # wait 10 seconds before looking for element "Create Review Request button"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH," //div[@class='RecordActionWidget---button_layout_inner_wrapper']//button[text()='Create Review Request']")))
        element.click()
    except:
        print("Unable to click on Create Review Button")

    # Adding Title ,Folder & Period  on Create Review Request Page
    else:
        Title = driver.find_element_by_xpath("//div[@class='FieldLayout---field_layout FieldLayout---margin_below_standard FieldLayout---margin_above_none']//div[@class='FieldLayout---input_below']//input")
        Title.send_keys("Testing Review Automated Title New")
        #Selecting Folder on Create Review Request Page
        Folder_field=driver.find_element_by_xpath("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder DropdownWidget---inSideBySideItem']")
        Folder_field.click()
        #Selecting value of Folder field from dropdown
        action = ActionChains(driver)
        action.key_down(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ENTER).perform()
        #Selecting Period on Create Review Request Page
        Period_field=driver.find_element_by_xpath("//div[@class='DropdownWidget---dropdown_value DropdownWidget---placeholder DropdownWidget---inSideBySideItem']")
        Period_field.click()
        #Selecting value of Period field from dropdown
        action = ActionChains(driver)
        action.key_down(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ENTER).perform()

#Selecting Reviewer on Create Review Request Page & Press Enter key
    try:
        Reviewer_1=driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[1]//input")
        Reviewer_1.send_keys("nisha")
        time.sleep(2)
        action = ActionChains(driver)
        action.key_down(Keys.ENTER).perform()
        time.sleep(2)
    except:
        print("Unable to add Reviewer 1 in the Reviewer list")

#Click on Add Reviewer link under workflow section and Add second Reviewer
    try:
        Add_Reviewer_link=driver.find_element_by_xpath("//a[contains(text(),'Add Reviewer')]")
        Add_Reviewer_link.click()
        time.sleep(2)
        Reviewer_2=driver.find_element_by_xpath("//div[@class='ContentLayout---content_layout ContentLayout---padding_less']//tr[2]//input")
        Reviewer_2.send_keys("Raw")
        time.sleep(2)
        action.key_down(Keys.ENTER).perform()
        time.sleep(2)
    except:
        print("Either unable to  click on Add Reviewer Link or unable to add Reviwer 2 in the Reviewer list")

#Adding Description on Create Review Request Page
    try:
        Title.click() # by using tab or action key method clicked on Bold button
        action.send_keys(Keys.TAB * 6).perform() # Reached on Bold button in description editor
        time.sleep(2)
        action.send_keys(Keys.ENTER).perform()
        TEXT = "Testis a long established fact that a reader will be distracted by the readable content of a page when looking at its layout." # Adding Description
        pyperclip.copy(TEXT) # use to copy the text on clipboard
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # Use to paste the text using action chains
    except:
        print("Unable to add text in Description section")
    #Scroll down and click on Add document link
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

#Click on Add Document Link
    try:
        Add_document=driver.find_element_by_xpath("//a[contains(text(),'Add Document')]")
        Add_document.click()
        time.sleep(2)
        # Add Title under Documents section
        Document_title=driver.find_element_by_xpath("//tbody//tr/td[1]/div/input")
        Document_title.send_keys("Doc test title")
        # Click on Link Radio button
        Radio_button_selection=driver.find_element_by_xpath("//div[@class='RadioSelect---choice_pair']//label[contains(text(),'Link')]")
        Radio_button_selection.click()
        time.sleep(2)
        #Add Document/Link text
        Adding_link=driver.find_element_by_xpath("//div[@class='EditableGridLayout---scrollable_content']//td[3]//input")
        Adding_link.send_keys("https://rally1.rallydev.com")
        # Add description for link
        link_description=driver.find_element_by_xpath("//td[@class='EditableGridLayout---reducedPadding'][3]/div/textarea")
        link_description.send_keys("Testing description")
    except:
        print("Unable to add data in Document section in any one field")

#Click on Submit Button
    try:
        Save_button=driver.find_element_by_xpath("//button[text()='SUBMIT']")
        Save_button.click()
    except:
        print("Unable to click on Submit button")



