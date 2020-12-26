from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

name = input("Enter the contact or Group name: ")
message = input("Enter the spam message: ")
count = int(input("Enter the number of times the mesage has to be send: "))
input("\n\tPress enter after scanning the qr code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1awRl copyable-text selectable-text')
msg_box.click()

for i in range(count):
    msg_box.send_keys(message + Keys.ENTER)