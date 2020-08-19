from selenium import webdriver
import time

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

    def get_url(self, url="http://testautomationpractice.blogspot.com/"):
        self.driver.get(url)
        self.driver.maximize_window()
        print(self.driver.current_url)
        print(self.driver.title)

    def close_browser(self):
        self.driver.close()
