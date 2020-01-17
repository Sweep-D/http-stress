

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


count = 0
browser = webdriver.Chrome()
url = input("Enter Browser URL:")

while count < 100:
    browser.get(url)
    browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
    print("Currently at ", count)
    count += 1