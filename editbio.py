# Import file datecount.py
from datecount import *

# Import selenium Keys
from selenium.webdriver.common.keys import Keys

# Get day from function getDays() in datecount.py
days = getDays()


class EditBio:
    def __init__(self, driver):
        
        # Go edit url to go stright to edit profile
        driver.get("https://www.instagram.com/accounts/edit/")
        
        # Get the edit bio box element
        bio = driver.find_element_by_id("pepBio")
        
        # Check the days then send backspace to delete from end
        # Example: It's been 10 days.
        # Because the code point the cursor at the end of string.
        # So from example I press backspace 6 times and get: It's been
        # I don't know why it have to -2 times but it work, so yeah...
        if days <= 10:
            bio.send_keys(6 * Keys.BACKSPACE)
        elif days <= 100:
            bio.send_keys(7 * Keys.BACKSPACE)
        elif days <= 1000:
            bio.send_keys(8 * Keys.BACKSPACE)
        elif days <= 10000:
            bio.send_keys(9 * Keys.BACKSPACE)
        elif days <= 100000:
            bio.send_keys(10 * Keys.BACKSPACE)
        
        # Then I send new string with new days in it
        bio.send_keys("{} days.".format(days))
        
        # This find the submit button, its div class name is 'fi8zo'
        # and that div have button so point directly to it
        # I hope Instagram won't change it because I hate to edit the code.
        send = driver.find_element_by_class_name('fi8zo')
        sendex = send.find_element_by_xpath("button")
        
        # And click the button
        sendex.click()
