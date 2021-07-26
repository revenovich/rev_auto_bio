# Import selenium By
from selenium.webdriver.common.by import By

# Import selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

# Import selenium WebDriverWait expected_conditions
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver, usern, passw):
        try:
            # Wait for the login form to appear
            # I use element login button so I can reuse it to click
            login = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')) # html xpath of login button
            )

            # Find username field and input username
            username = driver.find_element_by_name("username")
            username.send_keys(usern)

            # Find password field and input password
            password = driver.find_element_by_name("password")
            password.send_keys(passw)

            # Click login button
            login.click()
            StoreInfo(driver)
        except:
            print("Error at Login")
        

class StoreInfo:
    def __init__(self, driver):
        try:
            # Wait for the store info form to appear
            # I use element cmbtv. It contain not store info button so I can reuse it
            info = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cmbtv'))
            )
            
            # Find the button
            notstore = info.find_element_by_xpath("button")
            
            # Click the button
            notstore.click()
        except:
            print("Error at StoreInfo")
