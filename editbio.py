from datecount import *



from selenium.webdriver.common.keys import Keys


class EditBio:
    def __init__(self, driver):
        driver.get("https://www.instagram.com/accounts/edit/")
        bio = driver.find_element_by_id("pepBio")
        if getDays() <= 100000:
            bio.send_keys(10 * Keys.BACKSPACE)
        elif getDays() <= 10000:
            bio.send_keys(9 * Keys.BACKSPACE)
        elif getDays() <= 1000:
            bio.send_keys(8 * Keys.BACKSPACE)
        elif getDays() <= 100:
            bio.send_keys(7 * Keys.BACKSPACE)
        elif getDays() <= 10:
            bio.send_keys(6 * Keys.BACKSPACE)
        bio.send_keys("{} days.".format(getDays()))
        send = driver.find_element_by_class_name('fi8zo')
        sendex = send.find_element_by_xpath("button")
        sendex.click()

        if getDays() and getDays() is not None:
            date = getDays()


