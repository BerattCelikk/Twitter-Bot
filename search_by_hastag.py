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


    def search(self,hastag):
        search_input=self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
        search_input.send_keys(hastag)
        time.sleep(3)

        search_input.send_keys(Keys.ENTER)
        
        time.sleep(3)
        list=self.browser.find_elements(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[5]/section/div/div/div[2]/div/div/article")
        for i in list:
            print(i.text)

username = input("Username: ")
password = getpass.getpass("password: ")




x = X(username, password)
x.signin()
ssearch=input("What do you want to search for?")
x.search(ssearch)

input("Press Enter to close the browser")
x.browser.quit()
