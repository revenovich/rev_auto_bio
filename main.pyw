from selenium import webdriver
import login as lg
import editbio as eb

PATH = ".\\chromedriver.exe"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"

username = ""
password = ""


class Main:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--log-level=2")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(PATH, options=self.options, service_args=["--verbose", "--log-path=.\\wd.log"])
        self.action = webdriver.ActionChains(self.driver)

    try:
        def ig_run(self):
            self.driver.get("https://www.instagram.com/accounts/login/")

            lg.Login(self.driver, username, password)
            eb.EditBio(self.driver)
    except Exception as err:
        print(err)


Main().ig_run()
