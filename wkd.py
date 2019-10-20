from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import webbrowser

#setup
print("\n ************************************* \n\n Hi User, What do you want to search?")

search = input()

chrome_options = Options()

chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(executable_path = "drivers/chromedriver", options=chrome_options)

driver.maximize_window()

driver.get("https://www.youtube.com")

driver.find_element_by_name("search_query").send_keys(search)

driver.find_element_by_id("search-icon-legacy").click()

time.sleep(2)

driver.execute_script("window.open('https://www.google.com', 'new window')")

driver.switch_to.window(driver.window_handles[-1])

driver.find_element_by_xpath("//input[@type='text']").send_keys(search)

driver.find_element_by_name("btnK").click()
