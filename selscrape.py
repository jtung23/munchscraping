from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# imported to handle errors
from selenium.common.exceptions import NoSuchElementException

from csv import DictWriter

import time
import pprint
pp = pprint.PrettyPrinter(indent=4)
# starts on search results page
# clicks through into each

# sets up selenium driver and wait to properly interact with browser
driver = webdriver.Firefox()
wait = UI.WebDriverWait(driver, 5000)

site = "https://sfbay.craigslist.org/search/sfc/mar?query=social+media"
# opens firefox and goes to site
driver.get(site)

# creates list of links from search results
links = driver.find_elements_by_xpath('//a[contains(@class, "result-title")]')

# creates variable of search result page to focus back to
currentWindow = driver.current_window_handle 

# empty list to push data into
all_data = []

for each in links:
	new_data = {}
	# adds source url to dict(obj)
	new_data['source_url'] = each.get_attribute('href')
	# opens link in new tab
	each.send_keys(Keys.CONTROL + Keys.RETURN)
	time.sleep(2)
	# switches to new tab
	driver.switch_to.window(driver.window_handles[1])
	# explicit Selenium wait, when the reply button or "reply below" appears then continue
	elem = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".reply_button, .replybelow")))
	# if the class is replybelow then email is none
	elem_class = elem.get_attribute('class')
	if elem_class == 'replybelow':
		new_data['email'] = None
	# if class is reply_button then add email to dict
	else:
		elem.send_keys(Keys.RETURN)
		email_div = wait.until(
			lambda driver: driver.find_element_by_xpath('//p[contains(@class, "anonemail")]'))
		new_data['email'] = email_div.text
	# adds various info to dict(object)
	new_data['title'] = driver.find_element_by_xpath('//span[contains(@id, "titletextonly")]').text

	# tries for element, if does not exist, then replaces with none
	try:
		location_elem = driver.find_element_by_xpath('//span[contains(@class, "postingtitletext")]/small').text
		new_data['location'] = location_elem
	except NoSuchElementException:
		new_data['location'] = None

	try:
		compensation_elem = driver.find_element_by_xpath('//p[contains(@class, "attrgroup")]/span[contains(text(),"compensation")]/b').text
		new_data['compensation'] = compensation_elem
	except NoSuchElementException:
		new_data['compensation'] = None


	try:
		employment_elem = driver.find_element_by_xpath('//p[contains(@class, "attrgroup")]/span[contains(text(),"employment type")]/b').text
		new_data['employment_type'] = employment_elem
	except NoSuchElementException:
		new_data['employment_type'] = None
	# appends to list
	all_data.append(new_data)
	# closes tab
	driver.close()
	# switches focus to search results
	driver.switch_to_window(currentWindow)

# writes to csv file
with open('spreadsheet.csv','w') as outfile:
	# creates columns in sheets
    writer = DictWriter(outfile, ('title', 'email', 'source_url', 'location', 'compensation', 'employment_type'))
    writer.writeheader()
    # writes all data to excel sheet
    writer.writerows(all_data)