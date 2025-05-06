from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

'''
Please provide a clear and concise description of the actions performed by the code. 
The description should be written in a way that makes the code easy to understand and maintain. 
The code should be well-documented, so future developers can quickly grasp its functionality and 
make updates when necessary.
'''
class Testcase101:

    def main(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\Johny\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe") # Please use os lib of python to get the path of exe
        driver.get("https://interview.supporthive.com/staff/")
        driver.implicitly_wait(30)
        driver.maximize_window()

        # Verify the page has fully loaded after navigating to the URL by checking the presence of important web elements.
        # Please get the username and password from .env or environment variable
        driver.find_element(By.ID, "id_username").send_keys("Agent")
        driver.find_element(By.ID, "id_password").send_keys("Agent@123")
        driver.find_element(By.ID, "btn-submit").click()
        tickets = driver.find_element(By.ID, "ember29")
        action = ActionChains(driver)
        action.move_to_element(tickets).perform()
        statuses = driver.find_element(By.LINK_TEXT, "Statuses")
        statuses.click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/section/section/div/header/button").click() # Please use relative Xpath
        driver.find_element(By.TAG_NAME, "input").send_keys("Issue Created")
        statusColourSelect = driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']")
        statusColourSelect.click()
        statusColourEnter = driver.find_element(By.XPATH, "//input[@class='sp-input']")
        statusColourEnter.clear()
        statusColourEnter.send_keys("#47963f")

        '''
        Please use python 'Keys' lib to use escape
        Here Java key manager is been used.
        Below Python Snippet might be helpfull
        actions.send_keys(Keys.ESCAPE).perform()
        '''
        r = Robot()
        r.keyPress(KeyEvent.VK_ESCAPE)


        '''
        Don't use camelCase variable name structure in python please use snake_case structure
        first_element
        second_element

        Note: camelCase is encourage in Java and Javascript
        
        please give proper meaning full name for variables
        '''
        firstElement = driver.find_element(By.XPATH, "//a[@id='first-link']")
        firstElement.click()
        secondElement = driver.find_element(By.XPATH, "//a[@id='second-link']")
        secondElement.click()
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Status when a new ticket is created in HappyFox")
        addCreate = driver.find_element(By.XPATH, "//button[@class ='hf-entity-footer_primary hf-primary-action ember-view']")
        addCreate.click() 
        time.sleep(3) # Use implicitly_wait instead of static wait
        moveTo = driver.find_element(By.XPATH, "//td[@class ='lt-cell align-center hf-mod-no-padding ember-view']")
        action.move_to_element(moveTo).perform()
        moveTo.click()
        time.sleep(9) # Use implicitly_wait instead of static wait
        issue = driver.find_element(By.XPATH, "//div[contains(text(),'Issue Created')]")
        action.move_to_element(issue).perform()
        make = driver.find_element(By.LINK_TEXT, "Make Default")
        make.click()
        driver.find_element(By.LINK_TEXT, "Priorities").click()
        driver.find_element(By.XPATH, "//header/button[1]").click()  # Please use relative Xpath
        driver.find_element(By.TAG_NAME, "input").send_keys("Assistance required")
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Priority of the newly created tickets")
        button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']")
        button.click()
        time.sleep(9) # Use implicitly_wait instead of static wait
        tickets2 = driver.find_element(By.ID, "ember29")
        action.move_to_element(tickets2).perform()
        priorities2 = driver.find_element(By.LINK_TEXT, "Priorities")
        priorities2.click()
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[9]/td[2]").click() # Please use relative Xpath
        driver.find_element(By.LINK_TEXT, "Delete").click()
        delete = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']")
        delete.click()
        # Confirm its deleted 
  
        time.sleep(9) # Use implicitly_wait instead of static wait
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/header[1]/div[2]/nav[1]/div[7]/div[1]/div[1]").click() # Please use relative Xpath
        driver.find_element(By.LINK_TEXT, "Logout").click()
        # Confirm Logout

class PagesforAutomationAssignment:

    def main(self):
        driver = webdriver.Chrome()
        driver.get("https://www.happyfox.com")

        loginPage = LoginPage(driver)
        # Please get the username and password from .env or environment variable
        loginPage.login("username", "password")

        homePage = HomePage(driver)
        homePage.verifyHomePage()

        driver.quit()

class BasePage:

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()
        # Verify Login

    def forgotPassword(self): # please use snake_case structure
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()

class HomePage(BasePage):

    def verifyHomePage(self): # please use snake_case structure
        if self.driver.current_url != "https://www.happyfox.com/home":
            raise Exception("Not on the home page")

    # please use snake_case structure
    def navigateToProfile(self):
        self.driver.find_element(By.ID, "profileLink").click()
               
'''
This class `TablePage` is currently not used anywhere in the provided codebase.
Please clarify its purpose or remove it if it's unnecessary to avoid dead code.
'''
class TablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.rowLocator = By.XPATH("//table[@id='dataTable']/tbody/tr")
 
    def retrieveRowTexts(self): # please use snake_case structure
        rows = self.driver.find_elements(self.rowLocator)

        for i in range(len(rows)):
            row = rows[i]
            rowText = row.text # Changed to snake_case
            print("Row " + str(i) + " Text: " + rowText) # Please use format string method

