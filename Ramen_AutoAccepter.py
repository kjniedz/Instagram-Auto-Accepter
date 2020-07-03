import requests
import time
import os
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
configfile = os.path.join(ROOT_PATH, "config.ini")
executable_path = os.path.join(ROOT_PATH, "chromedriver.exe")

config = configparser.ConfigParser(interpolation=None)
config.read(configfile)
secret = config["SETTINGS"]
username = str(secret["username"])
password = str(secret["password"])
delay = int(secret["delay"])

url = "https://www.instagram.com/accounts/login/?next=/accounts/activity/%3FfollowRequests%3D1"

print("Starting Session...")

chrome_options = ChromeOptions()

chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--log-level=OFF')

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path, chrome_options=chrome_options)
driver.get(url)

time.sleep(delay)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)

driver.find_element_by_xpath("(//div[contains(.,'Log In')])[7]").click()

print("Logged In!")

time.sleep(delay)

driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()

print("Listening for followers...")

while True:

	try:

		driver.find_element_by_xpath("//button[contains(.,'Confirm')]").click()
		driver.refresh()
	except:
		driver.refresh()

os.system("pause")
driver.quit()