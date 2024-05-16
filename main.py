from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(r'https://www.browserstack.com/users/sign_up')


def get_element_by_id(type: str, val: str):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((type, val))
    )

    return element


full_name = get_element_by_id(By.ID, 'user_full_name')
full_name.send_keys('Naruto')
time.sleep(2)
email = driver.find_element(By.ID, "user_email_login")
email.send_keys('Naruto@hotmail.com')
time.sleep(2)

password = driver.find_element(By.ID, 'user_password')
password.send_keys('Ichigo12!')
time.sleep(2)

checkbox = driver.find_element(By.ID, 'tnc_checkbox')
checkbox.click()
time.sleep(2)

accept_cookie = get_element_by_id(By.ID, 'accept-cookie-notification')
accept_cookie.click()
time.sleep(2)


submit_details = get_element_by_id(By.NAME, 'commit')
submit_details.click()


"""

Will automatically sign up into this website and use the details i passed in!!!

"""

