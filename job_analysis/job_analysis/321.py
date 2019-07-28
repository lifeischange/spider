# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def process_request():
    driver=Firefox()
    action=ActionChains(driver)
    driver.get('https://www.zhipin.com')
    #driver.find_element_by_xpath('//input[@name="query"]').send_keys("shujufenxi")
    #search=driver.find_element_by_xpath('//button[@ka="search_box_index"]')
    #action.move_to_element(search)
    #action.click(search)
    #action.perform()
    job_list=driver.find_elements_by_xpath('//div[@class="city-box"]/div[@class="dorpdown-city"]/ul/li')
    print(job_list)
    for i in job_list:
        
        print(i.get_attribute('data-val'))
    
    print('/////////////')

if __name__=='__main__':
    process_request()
