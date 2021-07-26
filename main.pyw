# Import selenium webdriver
from selenium import webdriver

# Import login.py
import login as lg

# Import editbio.py
import editbio as eb

# Declare path of chromedriver.exe
PATH = ".\\chromedriver.exe"

# Declare user_agent for headless browser. If not Instagram will block the script
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"

# Declare username and password
username = ""
password = ""


class Main:
    def __init__(self):
        
        # All chrome webbrowser options.
        # You can find its document at https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.options
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
        
        # Init the driver and set it to log everytime run
        self.driver = webdriver.Chrome(PATH, options=self.options, service_args=["--verbose", "--log-path=.\\wd.log"])
        
        # Init driver action chain
        self.action = webdriver.ActionChains(self.driver)

    try:
        def ig_run(self):
            # Go to Instagram login
            self.driver.get("https://www.instagram.com/accounts/login/")
            
            # Run login function
            lg.Login(self.driver, username, password)
          
            # Run edit bio function
            eb.EditBio(self.driver)
    except Exception as err:
        print(err)

# Run run run :D
Main().ig_run()
