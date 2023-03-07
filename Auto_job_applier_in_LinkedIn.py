from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException, ElementNotInteractableException
chrome_driver_path = r"C:\Users\LENOVO\OneDrive\Documents\Driver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3095503622&f_AL=true&geoId=103644278&keywords=software%20engineer&location=United%20States&sortBy=R')



time.sleep(2)
sign_in = driver.find_element_by_class_name('nav__button-secondary')
sign_in.click()

time.sleep(5)
username = driver.find_element_by_id('username')
username.send_keys('sampadedge@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('Sam@2022')
password.send_keys(Keys.ENTER)


# for single job
# job_link = driver.find_element_by_class_name('job-card-container__link')
# if job_link.text=='Senior Data Engineer':
#     job_link.click()

# easy_apply = driver.find_element_by_class_name('jobs-apply-button')
# easy_apply.click()

# phone_number = driver.find_element_by_class_name('fb-single-line-text__input')
# phone_number.send_keys('1234567890')

# submit = driver.find_element_by_class_name('artdeco-button--primary')
# submit.click()



# for multiple jobs
time.sleep(3)
buttons = driver.find_elements_by_css_selector('.msg-overlay-bubble-header__controls button')
button_ids = [button.get_attribute('id') for button in buttons]
drop_down = driver.find_element_by_id(button_ids[2])
drop_down.click()

time.sleep(2)
job_titles = driver.find_elements_by_css_selector('.job-card-list__title')

for job in job_titles:
    time.sleep(3)
    print('called')
    job.click()
    time.sleep(2)

    # try to locate apply button, if not found then skip the job
    try:
        
        easy_apply = driver.find_element_by_css_selector('.jobs-s-apply button')
        easy_apply.click()
        time.sleep(2)

        # if phone field is empty then add number
        phone = driver.find_element_by_class_name('fb-single-line-text__input')
        if phone.text == "":
            phone.send_keys('1234567890')
        
        submit_button = driver.find_element_by_css_selector('footer button')

        # if submit button is a next button, then multistep process, so skip
        if submit_button.text != 'Submit application':
            exit_button = driver.find_element_by_class_name('artdeco-modal__dismiss')
            exit_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_css_selector('.artdeco-modal--layer-confirmation .artdeco-button--secondary')
            discard_button.click()
            print('Complex Application Skipped')
            continue
        else:
            submit_button.click()
        
        # once application is over close the pop-up window
        time.sleep(2)
        close_button = driver.find_element_by_css_selector('.artdeco-toast-item__dismiss')
        close_button.click() 
    except NoSuchElementException:
        print('No application button. Skipped.')
        continue
    try:
        job.click()
    except StaleElementReferenceException:
        continue
    except ElementNotInteractableException:
        continue










