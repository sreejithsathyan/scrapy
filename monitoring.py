from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
import time

browser = webdriver.Chrome()
browser.get(
    "https://sprintcso.marketing.adobe.com/content/mac/sprintcso/managedservices/nagios.html")
browser.find_element_by_id('mac-ims-login').click()
browser.find_element_by_xpath('//*[@id="adobeid_username"]').send_keys('#######')
browser.find_element_by_id("adobeid_password").click()
time.sleep(2)
browser.find_element_by_id("adobeid_password").send_keys("#######")
login_attempt = browser.find_element_by_id('sign_in')
login_attempt.submit()
link = browser.find_elements(By.XPATH, '//div[@class="app"]/a')

warning_url = []
critical_url = []
warning = []
critical = []

for data in link:
    html = data.get_attribute('innerHTML')
    if 'Warning' in html:
        warning_url.append(data.get_attribute('href'))
    elif 'Critical' in html:
        critical_url.append(data.get_attribute('href'))
for url in warning_url:
    browser.get(url)
    link = browser.find_elements(By.XPATH, '//div[@class="app"]')
    for data in link:
        html_data = data.get_attribute('innerHTML')
        sel = Selector(text=html_data)
        if 'orange' in html_data:
            warning.append(sel.xpath('//h3/center/text()').extract_first())
        elif 'red' in html_data:
            critical.append(sel.xpath('//h3/center/text()').extract_first())
print('Warning_Error', '\n', 'Warning:', warning, '\n', 'Critical:', critical)
warning = []
critical = []
for url in critical_url:
    browser.get(url)
    link = browser.find_elements(By.XPATH, '//div[@class="app"]')
    for data in link:
        html_data = data.get_attribute('innerHTML')
        sel = Selector(text=html_data)
        if 'orange' in html_data:
            warning.append(sel.xpath('//h3/center/text()').extract_first())
        elif 'red' in html_data:
            critical.append(sel.xpath('//h3/center/text()').extract_first())
print('Critical_Error', '\n', 'Warning:', warning, '\n', 'Critical:', critical)
