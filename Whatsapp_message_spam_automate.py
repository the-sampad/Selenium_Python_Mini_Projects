# Auto WhatsApp messenger
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = r"C:\Users\LENOVO\OneDrive\Documents\Driver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

NAME = "Just H"

driver.get('https://web.whatsapp.com/')

time.sleep(30)
update = driver.find_element_by_css_selector("._1XkO3 ._2z7gr")
update.click()

# time.sleep(3)
# contacts = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div/span')
# contacts.click()

time.sleep(20)
search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
search_box.send_keys(NAME)

time.sleep(2)
chats = driver.find_elements_by_css_selector('._3Bc7H .zoWT4 span.matched-text.i0jNr')

time.sleep(2)
for chat in chats:
    if chat.text == NAME:
        chat.click()


        time.sleep(3)
        for i in range(1000000):
            text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
            text_box.send_keys('Hazrat ! Hazrat ! Hazrat ! Third Sem aa raha hai !!!')
            text_box.send_keys(Keys.ENTER)
            
    







