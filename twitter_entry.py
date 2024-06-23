import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class X:
    def __init__(self, username, password):
        self.browser_options = webdriver.ChromeOptions()
        self.browser_options.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
        self.browser = webdriver.Chrome(options=self.browser_options)
        self.username = username
        self.password = password
        
    def signin(self):
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(5)
        
        try:
            username_input = self.browser.find_element(By.NAME, "text")
            username_input.send_keys(self.username)
            username_input.send_keys(Keys.ENTER)
            time.sleep(2)
            
            password_input = self.browser.find_element(By.NAME, "password")
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.ENTER)
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")


username = input("Username: ")
password = getpass.getpass("password: ")


x = X(username, password)
x.signin()

input("Press enter to close X (Twitter)")
x.browser.quit()
