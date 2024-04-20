# CUSTOMER BOT PROGRAM, COMMENTS INCLUDED FOR CLIENTS SAKE
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import urllib
import urllib.request
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
urllib.request.urlcleanup()


def typeSpeed(element: WebElement,text:str):
    ''' function for typing for captcha at a human speed'''
    delay = 0.2
    for char in text:
        element.send_keys(char)
        time.sleep(delay)
options = webdriver.ChromeOptions() 
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://vanlawn.com/Login_(1).aspx")
print('trying')
type1 = driver.find_element(By.XPATH,
                            '//*[@id="p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_UserName"]')
        
        # find password input field and insert password as well
typeSpeed(type1,"7260a")
time.sleep(0.5)
type2 = driver.find_element(By.XPATH,

                            '//*[@id="p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_Password"]')
typeSpeed(type2,"Bunnyof2")
elm = driver.find_element(By.ID,"p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_LoginButton")
driver.execute_script("arguments[0].click();", elm)
i = input('wait')



