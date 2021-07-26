from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver, usern, passw):
        try:
            login = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))
            )

            username = driver.find_element_by_name("username")
            username.send_keys(usern)

            password = driver.find_element_by_name("password")
            password.send_keys(passw)

            login.click()
        except:
            print("Error at Login")
        StoreInfo(driver)


class StoreInfo:
    def __init__(self, driver):
        try:
            info = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cmbtv'))
            )

            notstore = info.find_element_by_xpath("button")
            notstore.click()
        except:
            print("Error at StoreInfo")
