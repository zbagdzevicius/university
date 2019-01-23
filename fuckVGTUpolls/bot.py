from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from platform import system
from time import sleep
import os
import sys
from subprocess import call

username = ''
password = ''

class BOT():
    def __init__(self, username, password):
        self.loadingSleepTime = 1
        self.driver = self.getDriver()
        self.login(username, password)
        self.completePolls()
    
    def getDriver(self):
        driverPath = self.getDriverPath(system())
        driver = webdriver.Chrome(driverPath)
        return driver
    
    def getDriverPath(self, operatingSystem):
        cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
        chromeDriverPath = None
        if system() == 'Windows':
            chromeDriverPath = f'{cwd}/chromedriverWin.exe'
        elif system() == 'MacOS':
            chromeDriverPath = f'{cwd}/chromedriverMac'
        else:
            chromeDriverPath = f'{cwd}/chromedriverLinux'
            call(["chmod","+x",chromeDriverPath])
        return chromeDriverPath
    
    def login(self, username, password):
        self.driver.get('https://mano.vgtu.lt')
        usernameField = self.wait_until_element_located("input#username")
        usernameField.send_keys(username)
        passwordField = self.wait_until_element_located(".password input")
        passwordField.send_keys(password)
        submitButton = self.wait_until_element_located("input[type='submit']")
        submitButton.submit()

    def completePolls(self):
        polls = self.getPolls()
        pollURLs = []

        for poll in polls:
            pollURL = poll.get_attribute('href')
            pollURLs.append(pollURL)

        for pollURL in pollURLs:
            self.driver.get(pollURL)
            while True:
                try:
                    self.completePoll()
                except:
                    break

                
    def getPolls(self):
        sleep(self.loadingSleepTime)
        polls = self.driver.find_elements_by_css_selector('.el_var_block.with_arrow.with_hover .btn_wrapper a')
        return polls
    
    def completePoll(self):
        moveNextButton = self.wait_until_element_located('#movenextbtn')
        self.clickElseSubmit(moveNextButton)
        radioButtons = self.getRadioButtons()
        for radioButton in radioButtons:
            radioButton.click()
        maximumPagesInPoll = range(4)
        for page in maximumPagesInPoll:
            try:
                confirmButton = self.wait_until_element_located('#movenextbtn')
                self.clickElseSubmit(confirmButton)
                sleep(self.loadingSleepTime)
            except:
                confirmButton = self.wait_until_element_located('#movesubmitbtn')
                self.clickElseSubmit(confirmButton)
        
    def clickElseSubmit(self, element):
        try:
            element.click()
        except:
            element.submit()
        
    def getRadioButtons(self):
        sleep(self.loadingSleepTime)
        radioButtons = self.driver.find_elements_by_css_selector('.radio')[::4]
        return radioButtons

    def wait_until_element_located(self, css_selector):
        waiting = WebDriverWait(driver=self.driver, timeout=self.loadingSleepTime*2)
        element_to_wait = waiting.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        return element_to_wait

BOT(username,password)