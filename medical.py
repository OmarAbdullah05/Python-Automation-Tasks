from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


#setup
print("\n ************************************* \n\n Hi Omar, What do you want to search?")

search = input()

URL = 'https://www.medicinenet.com/script/main/hp.asp'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

#selenium section

chrome_options = Options()

chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(executable_path = "drivers/chromedriver", options=chrome_options)

driver.get(URL)

driver.find_element_by_xpath("//input[@class='sc-searchbox-input']").send_keys(search)

driver.find_element_by_xpath("//div[@class='sc-modal-dialog roadblock']/div[@class='sc-modal-content' and 1]/div[@class='sc-modal-header' and 1]/a[@class='close sc-modal-button' and 1]").click()

driver.find_element_by_xpath("//button[@class='sc-searchbox-button icon-search']").click()

driver.find_element_by_xpath("//div[@class='searchresults sym']/ul[1]/li[1]/a[1]").click()

#second link: driver.find_element_by_xpath("//div[@class='searchresults sym']/ul[1]/li[2]/a[1]").click()

resOne = driver.find_element_by_xpath("//div[@class='apPage']/p[2]")

print("\n")
print(resOne.text)
print("\n")
