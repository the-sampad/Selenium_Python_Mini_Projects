

# My own Code 
# NO errors detected while testing for 5 times with my credentials
# Constants and variables changed later for public usage


import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = r"C:\Users\LENOVO\OneDrive\Documents\Driver\chromedriver.exe"

USERNAME = 'Enter your Gmail Username'
PASSWORD = 'Enter password'
FORM_LINK = 'Enter the public google form link'
FORM_LINK_RESPONSES = 'Enter form link from responses page'

url = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=&cityName=Mumbai&category=B&parameter=rel&hideviewed=N&ListingsType=I&filterCount=3&incSrc=Y&fromSrc=homeSrc'
response = requests.get(url)

data = response.text
soup = BeautifulSoup(data, 'html.parser')

property_name_tags = soup.find_all('h2', class_='mb-srp__card--title')
property_names = []
for property in property_name_tags:
    name = property.text
    property_names.append(name)

price_tags = soup.find_all('div', class_='mb-srp__card__price--amount')
prices = []
for price_tag in price_tags:
    price = price_tag.text
    prices.append(price)

owner_name_tags = soup.find_all('div', class_='mb-srp__card__ads--name')
owners = []
for owner_tag in owner_name_tags:
    owner = owner_tag.text
    owners.append(owner)


# Use Selenium to use the data and fill a google for and then converting that form into a spreatsheet at the end 

driver = webdriver.Chrome(chrome_driver_path)

for i in range(len(property_names)):
    
    driver.get(FORM_LINK)
    time.sleep(2)

    property_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    owner_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        
    property_field.send_keys(property_names[i])
    owner_field.send_keys(owners[i])
    price_field.send_keys(prices[i])
    submit.click()
    time.sleep(2)
driver.close()
time.sleep(2)

form = uc.Chrome(use_subprocess=True)
form.get('https://www.google.com/')
form.maximize_window()
time.sleep(2)
signin = form.find_element_by_link_text('Sign in')
signin.click()
time.sleep(2)
username_field = form.find_element_by_xpath('//*[@id="identifierId"]')
username_field.send_keys(USERNAME)
username_field.send_keys(Keys.ENTER)
time.sleep(2)
password_field = form.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(3)
form.get(FORM_LINK_RESPONSES)
time.sleep(4)
options = form.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[2]/div/div/span/span/div/div[3]')
options.click()
time.sleep(2)
option_2 = form.find_elements_by_css_selector('div.JAPqpe.K0NPx span')
option_2[1].click()
time.sleep(2)
create = form.find_element_by_css_selector('div.OE6hId.J9fJmf div.uArJ5e.UQuaGc.kCyAyd.l3F1ye.ARrCac.HvOprf.M9Bg4d')
create.click()
time.sleep(2)
spreadsheet = form.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span/div/div[1]')
spreadsheet.click()
time.sleep(60*60*24)

form.exit()












