

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

count = 0
url = input("Enter Browser URL:")
client = webdriver.Chrome()

while count < 100:
    print("Currently ran this ", count)
    client.get(url)
    count += 1
    