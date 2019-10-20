from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


print("\n ************************************* \n\n Hi User, What do you want to name your repo?")

name = input()

print("\n What do you want your repo description to be?")

desc = input()

chrome_options = Options()

chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(executable_path = "chromedriver", options=chrome_options)

driver.maximize_window()

driver.get("https://www.github.com")

driver.find_element_by_xpath("//a[@class='HeaderMenu-link no-underline mr-3']").click()

driver.find_element_by_name("login").send_keys("$email")

driver.find_element_by_name("password").send_keys("Password")

driver.find_element_by_name("commit").click()

driver.find_element_by_xpath("//div[@class='mb-3 Details js-repos-container mt-5']/div[@class='js-repos-container' and 1]/h2[1]/a[@class='btn btn-sm btn-primary text-white' and 1]").click()

driver.find_element_by_xpath("//input[@id='repository_name']").send_keys(name)

driver.find_element_by_xpath("//input[@id='repository_description']").send_keys(desc)

driver.find_element_by_xpath("//input[@id='repository_auto_init']").click()

driver.find_element_by_xpath("//button[@class='btn btn-primary first-in-line']").click()
