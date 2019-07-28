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
    driver.find_element_by_xpath('//input[@name="query"]').send_keys("shujufenxi")
    search=driver.find_element_by_xpath('//button[@ka="search_box_index"]')
    action.move_to_element(search)
    action.click(search)
    action.perform()
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"job-title")))
    job_list=driver.find_elements_by_xpath('//div[@class="job-title"]')
    
    print('/////////////')
    for job in job_list:
        print(job.text)
        #job_detail=driver.find_element_by_xpath('//div[@class="job-title"]') 
        action=ActionChains(driver)
        action.move_to_element(job)
        time.sleep(5)
        action.perform()
        #wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='detail-bottom-title']")))
        try:
            print(driver.find_element_by_xpath('//div[@class="info-detail"]').text)
           # wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='detail-bottom-title']")))            
           # time.sleep(1)
        except:
            print("no found")
        #action.perform()
        #raise "stop"
        #print(driver.find_element_by_xpath('//div[@class="detail-buttom-text"]').text)
        print('++++++++++++++')
    driver.close()
    return None


if __name__=='__main__':
    process_request()
