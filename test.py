from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
import pprint
pp = pprint.PrettyPrinter(indent=4)
# starts on search results page
# clicks through into each

driver = webdriver.Firefox()
wait = UI.WebDriverWait(driver, 5000)

driver.get('https://sfbay.craigslist.org/sfc/mar/d/marketing-communication/6461430138.html')

# # # once on each indiv site
elem = driver.find_element_by_class_name('reply_button')
elem.send_keys(Keys.RETURN)
email_div = wait.until(
	EC.visibility_of_element_located((By.CSS_SELECTOR, ".returnemail")))

anon_email = driver.find_element_by_xpath('//p[contains(@class, "anonemail")]')
print(anon_email.text)