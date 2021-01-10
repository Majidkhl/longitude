import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from logzero import logger
import selenium.common.exceptions as exception
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from openpyxl.workbook import Workbook

# Use the headless option to avoid opening a new browser window
options = webdriver.ChromeOptions()
options.add_argument("headless")
desired_capabilities = options.to_capabilities()
driver = webdriver.Chrome(desired_capabilities=desired_capabilities)


path = 'C:/Users/a_khl/PycharmProjects/selenium/data/'

# driver = webdriver.Chrome()

url = 'https://www.google.fr/maps/'

driver.get(url)
search_key = "145 East Harmon Avenue, Las Vegas, NV 89109-4504"

search = driver.find_element_by_id("searchbox")

# search.send_keys(search_key)
# time.sleep(5)
# search.send_keys(Keys.RETURN)

search.submit()
time.sleep(1)

# print(driver.current_url)

# courses_list = []
# titles = driver.find_elements_by_class_name('btntitle')
# for title in titles:
#    courses_list.append(title.text)
#
# # while True:
# for i in range(1, 1000):
#    try:
#       # next_page_button = driver.find_element_by_xpath("//button[contains(.,'Next Page »')]") # works also
#       next_page_button = driver.find_element(By.XPATH, '//button[text()="Next Page »"]')
#       next_page_button.click()
#       titles = driver.find_elements_by_class_name('btntitle')
#       for title in titles:
#          courses_list.append(title.text)
#
#    except NoSuchElementException:
#       logger.debug(f"Last page reached for {search_key}")
#       break



# Implicit wait
# driver.implicitly_wait(10)
# Explicit wait
# wait = WebDriverWait(driver, 5)
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card__title")))


# driver.implicitly_wait(10)
# price = driver.find_element_by_xpath('div._36QMXqQj').text
# price = driver.find_element_by_class_name('_36QMXqQj').text

driver.quit()

# Write countries_list to json file
# with open("countries_list.json", "w") as f:
#     json.dump(countries_list, f)
#
# courses_df = pd.DataFrame(courses_list)
# courses_df.to_excel(f"{path}{search_key}.xlsx", sheet_name=f"{search_key}")
#
# print(courses_df)
# print(i)
