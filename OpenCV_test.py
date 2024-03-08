#from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import urllib
import urllib.request
import time
from selenium.webdriver.remote.webelement import WebElement


urllib.request.urlcleanup()


def typeSpeed(element: WebElement,text:str):
    ''' function for typing for captcha at a human speed'''
    delay = 0.2
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


def captchaChecker(driver):
    ''' function for checks for captchas present '''
    try:
       web1 = WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']"))) 
       web2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
       return True
       
    except:
        return False
    


def click_element_by_xpath(driver, xpath, timeout=10):
    ''' function clicks web elements'''
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, xpath)))
    element.click()
    print('clicked at : ',datetime.datetime.now().time())


def book_c(day,court,p_court,p_time,hr,ball,courts):
    ''' function for booking court driver function '''
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    action = ActionChains(driver)
    driver.maximize_window()
    driver.implicitly_wait(10)

    
    def sign_out():
        ''' function signs out of account '''
        time.sleep(2)
        x_signout='/html/body/div[3]/div[2]/div[2]/div[1]/ul/li[3]/a'
        click_element_by_xpath(driver,x_signout)
        time.sleep(2)


    def login_tennis(day, court):
        '''function to login to tennis vbookinfg account'''
        print("Selected Day : "+str(day))
        print("Selected Court : "+str(court))
        day = day
        court = court
        driver.get("https://vanlawn.com/Login_(1).aspx")
        time.sleep(1)

        # find username/email field and send the username itself to the input field
        type1 = driver.find_element(By.XPATH,
                            '//*[@id="p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_UserName"]')
        
        # find password input field and insert password as well
        typeSpeed(type1,"7260a")
        time.sleep(0.5)
        type2 = driver.find_element(By.XPATH,

                            '//*[@id="p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_Password"]')
        typeSpeed(type2,"Bunnyof2")
        
        # click login button
        x_login='//*[@id="p_lt_ContentWidgets_pageplaceholder_p_lt_zoneContent_CHO_Widget_LoginFormWithFullscreenBackground_XLarge_loginCtrl_BaseLogin_LoginButton"]'
        click_element_by_xpath(driver, x_login)
        
        # Get the window handles to switch between them
        window_handles = driver.window_handles

        # Click on the element to open the new tab
        x_gt='//*[@id="main-menu"]/li[3]/a'
        click_element_by_xpath(driver,x_gt)
        # Wait for the new tab to open
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        # Switch to the new tab
        for handle in driver.window_handles:
            if handle != driver.current_window_handle:
                driver.switch_to.window(handle)
                break

        # Click on the Tennis in the new tab
        time.sleep(1)
        x_tennis='//*[@id="green_nav"]/div/ul/li[3]/a'
        click_element_by_xpath(driver,x_tennis)

        if day == 1:
            # Click on the element to select next 1 day activate it .
            x_day_one='//*[@id="dateSelector-picker"]/ul/li[2]/a/span'
            click_element_by_xpath(driver,x_day_one)
            time.sleep(2)

        if day == 2:
            # Click on the element to select next 2nd day activate it .
            x_day_two='//*[@id="dateSelector-picker"]/ul/li[3]/a/span'
            click_element_by_xpath(driver,x_day_two)
            time.sleep(2)

        # Click on the element to select Indoor Hard Courts 1 - 16
        if court == 1:
            pass

        if court == 2:
            x_court_2='//*[@id="groupHeader"]/span[2]'
            click_element_by_xpath(driver,x_court_2)

        if court == 3:
            x_court_3='//*[@id="groupHeader"]/span[3]'
            click_element_by_xpath(driver, x_court_3)

        if court == 4:
            x_court_4='//*[@id="groupHeader"]/span[4]'
            click_element_by_xpath(driver, x_court_4)

        time.sleep(1)


    def wait_tennis(p_court, p_time,hr,ball):
        '''function that waits for appropriate booking time'''
        while True:
            current_time = datetime.datetime.now().time()
            print('Current time : ',current_time)
            print('Finding courts...')
       
            if current_time >= datetime.time(hr-1, 59,0,1):
                bool = book_slot(p_court, p_time,ball,hr)
                if bool == False:
                    return False
                
                else:
                    return True


          


    def book_slot(p_court, p_time,ball,hr):
        ''' slot booking function'''
        p_court = p_court
        p_time = p_time
        ball=ball
        # Click on the element Slot
        x_slot='//*[@id="viewer"]/div[4]/table/tbody/tr/td[' + str(p_court) + ']/div[' + str(p_time) + ']'
        x_slotz='//*[@id="viewer"]/div[4]/table/tbody/tr/td[' + str(p_court) + ']/div'
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, x_slotz)))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, x_slot)))
        bool = False
        while bool == False:
            try:
                book = driver.find_element(By.XPATH,x_slot)
                time.sleep(1)
                bool = True
            except:
                print('cannot find element')
        booked_court = False
        #waiting for time to book
        if hr == 20:
            try:
                while driver.find_element(By.ID,'servertime').text != '7:59:59 pm':
                        pass
                time.sleep(0.99)
                book.click()
                print('Program clock ~6.5 seconds faster then tennis server clock, subtract that time from this...')
                print(datetime.datetime.now().time())

            except:
                print('court is booked ')

   
        else:
            try:
                while driver.find_element(By.ID,'servertime').text != '9:59:59 am':
                        pass
                time.sleep(0.99)
                book.click()
                print('Program clock ~6.5 seconds faster then tennis server clock, subtract that time from this...')
                print(datetime.datetime.now().time())
         
            except:
                print('court is booked')
      
        try:
            driver.find_element(By.XPATH,'//*[@id="timer"]')
            booked_court = True
        except:
            try:
                if driver.find_element(By.XPATH, '//*[@id="booking_err_detail"]').is_displayed()==True:
                    driver.back()
            except NoSuchElementException:
                print("Element doesn't exists")
 
            l = len(courts)
            _ = 0

            while _ < l:
                if courts[_] != p_court:
                    try:
                        x_slot='//*[@id="viewer"]/div[4]/table/tbody/tr/td[' + str(courts[_]) + ']/div[' + str(p_time) + ']'
                        click_element_by_xpath(driver,x_slot)
                        driver.find_element(By.XPATH,'//*[@id="timer"]')
                        _=l
                        booked_court = True

                    except:
                        try:
                            if driver.find_element(By.XPATH, '//*[@id="booking_err_detail"]').is_displayed()==True:                           
                                driver.back()
                                print('court booked, trying next one.')

                        except:
                            pass

                _+=1

        try:
            if driver.find_element(By.XPATH, '//*[@id="booking_err_detail"]').is_displayed()==True:
                error = driver.find_element(By.XPATH, '//*[@id="booking_err_detail"]').text
                print("Booking Error : " + error)
                return False
            
        except:
            if booked_court == False:
                print('no bookings available')
                return False

        time.sleep(1)

        print('ball 0')
        if ball==0:
            time.sleep(1)
            try:
                    if driver.find_element(By.XPATH, '//*[@id="bookingErrors"]').is_displayed()==True:
                        error = driver.find_element(By.XPATH, '//*[@id="bookingErrors"]').text
                        print("Booking Error : " + error + ", Court booking unavailable.")
                        return False
            
            except:
                    print('Court booking available')
       
            time.sleep(0.5)
            counter = 0
            #multiple attempts to type friend name
            while counter < 5:
                counter+=1
                try:
                    driver.find_element(By.XPATH, '// *[ @ id = "players[2][name]"]').send_keys("friend")
                    counter = 5

                except:
                    print('Cant type friend in.')

            #multiple attempts to click guest button
            while counter  > 0:
                counter-=1
                try:
                    x_guest_radio=' // *[ @ id = "players[2][guest]"]'
                    click_element_by_xpath(driver,x_guest_radio)
                    counter = 0

                except:
                    print('Cant find guest button.')

            time.sleep(1)
            flag = False
            #if captchaChecker(driver) == True:
                #print('Captcha defeated')
                #driver.switch_to.default_content()

            if flag == False:
                time.sleep(1)
                x_book_button='// *[ @ id = "btnBook"] / span'
                counter = 0

                #multiple attempts to book
                while counter < 5:
                    try:
                        click_element_by_xpath(driver,x_book_button)
                        counter = 5
                    except:
                        counter+=1
                  
                time.sleep(2)
                try:
                     driver.find_element(By.XPATH, '//*[@id="booking_err_detail"]').is_displayed()
                     error = driver.find_element(By.XPATH, '//*[@id="booking_err_detail"]').text
                     print("Booking Error : " + error)
                     return False
            
                except:
                    if booked_court == False:
                        print('no bookings available')
                        return False

                

        else:
            time.sleep(1)
            x_ball_m='//*[@id="rtype_22"]'
            click_element_by_xpath(driver,x_ball_m)
            time.sleep(1)
            x_ball_2='//*[@id="resources[5]"]'
            click_element_by_xpath(driver,x_ball_2)
            time.sleep(1)
            x_ball_submit='//*[@id="btnBook"]'
            x_ball_submit='//*[@id="btnBook"]/span'
            click_element_by_xpath(driver,x_ball_submit)
            print("Booking done with ball machine :")
            time.sleep(1)

    while True:
        current_time = datetime.datetime.now().time()
        print('Current time : ',current_time)

        if current_time >= datetime.time(hr-1, 57, 0, 2):
                try:
                    login_tennis(day, court)
                    bool = wait_tennis(p_court, p_time, hr,ball)
                    if bool == True:
                        print('Court successfully booked, signing out and  closing window.')
                        sign_out()
                        driver.quit()
                        return True
                    else:
                        print('Court unsuccessfully booked, signing out and  closing window.')
                        sign_out()
                        driver.quit()
                        return False
                    
                except:
                    print('network down cannnot access webpage.')
                    return False

          

