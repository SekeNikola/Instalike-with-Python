from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


class Instalike:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path='C:/webdrivers/chromedriver.exe')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_class_name(
            "sqdOP")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath(
            "//input[@name='email']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath(
            "//input[@name='pass']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        not_now_elem = driver.find_element_by_class_name(
            "HoLwm"
        )
        not_now_elem.click()
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 3):
            try:
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href)
                 for href in hrefs_in_view if href not in pic_hrefs]
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(60)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))

                def like_button(): return driver.find_element_by_xpath(
                    '//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    time.sleep(second)
            except:
                time.sleep(2)
            unique_photos -= 1


if __name__ == "__main__":

    username = "USERNAME"
    password = "PASSWORD"

    ig = Instalike(username, password)
    ig.login()

    hashtags = ['coding', 'python', 'javascript', 'development']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = Instalike(username, password)
            ig.login()
