from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.Chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pickle



options = Options()
options.headless = True
with webdriver.Chrome(options=options) as driver:
    
    page_num=0
    # lim 250
    page_lim=250
    links = []

    while(page_num < page_lim):    

        base_url = f'https://graduateland.com/da/jobs?types%5B%5D=3&types%5B%5D=2&positions%5B%5D=15&countries%5B%5D=6&limit=10&offset={page_num}'
        driver.get(base_url)
        
        root = WebElement


        divs = driver.find_elements_by_class_name('bem-enabled')

        for div in divs:
            try:
                temp = div.find_element_by_tag_name('a')
            except:
                continue
            lnk = temp.get_attribute('href')
            # print(lnk)
            links.append(lnk)
        page_num+=10
        print(page_num)
 
    
    # pickle save
    with open('listings.pkl', 'wb') as f:
        pickle.dump(links, f)
