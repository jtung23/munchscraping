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

driver.get("https://sfbay.craigslist.org/search/sfc/mar?query=social+media")

links = driver.find_elements_by_xpath('//a[contains(@class, "result-title")]')

currentWindow = driver.current_window_handle 
# all_links = [link.get_attribute('href') for link in links]


for each in links:
	new_data = {}
	each.send_keys(Keys.CONTROL + Keys.RETURN)
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[1])
	elem = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".reply_button, .replybelow")))
	elem_class = elem.get_attribute('class')
	print('elem class', elem_class)
	print('typeof', type(elem_class))
	if elem_class == 'replybelow':
		print('IS REPLYBELOW YIPPEE')
		new_data['email'] = None
	else:
		elem.send_keys(Keys.RETURN)
		email_div = wait.until(
			lambda driver: driver.find_element_by_xpath('//p[contains(@class, "anonemail")]'))
		new_data['email'] = email_div.text
	
	driver.close()
	driver.switch_to_window(currentWindow)

# # # once on each indiv site
# elem = driver.find_element_by_class_name('reply_button')
# elem.send_keys(Keys.RETURN)
# time.sleep(10)

# email_div = driver.find_element_by_xpath('/html/body/section/section/header/div[2]/aside/ul/li[1]/p/a')
# # print(email_div.text)