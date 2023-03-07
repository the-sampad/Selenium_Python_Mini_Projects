from selenium import webdriver
import time

chrome_driver_path = r"C:\Users\LENOVO\OneDrive\Documents\Driver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')


# get upgrade item ids
items = driver.find_elements_by_css_selector('#store div')
item_ids = [item.get_attribute('id') for item in items]

timeout = time.time() + 5
five_min = time.time()+ 60*60

while True:

    cookie.click()

    # every 5 seconds
    if time.time() > timeout:
        all_price_tags = driver.find_elements_by_css_selector('#store b')
        item_prices = []

        # converting <b> text to integer price
        for price in all_price_tags:
            price_text = price.text
            if price_text != "":
                cost = int(price_text.split('-')[1].strip().replace(',',''))
                item_prices.append(cost)
        

        # create dic for items and prices
        cookie_upgrades = {}
        for i in range(len(item_prices)):
            cookie_upgrades[item_prices[i]]=item_ids[i]
        
        # current cookie count
        cookie_ele = driver.find_element_by_id('money').text
        if ',' in cookie_ele:
            cookie_ele = cookie_ele.replace(',','')
        cookie_count = int(cookie_ele)

        # finding afforadable upgrades
        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        
        # purchase id of most expensive among the affordable items
        try:
            most_expensive_affordable_item = max(affordable_upgrades)
            purchase_id = affordable_upgrades[most_expensive_affordable_item]
        except ValueError:
            pass
        # purchase
        driver.find_element_by_id(purchase_id).click()


        # new timeout (adding another 5 seconds)
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id('cps').text
        print(cookie_per_s)
        break




