from crawlers import config

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getDynamicElement(driver , ticker : str):
    all_links = []
    driver.get(f'https://www.tradingview.com/symbols/BIST-{ticker}/news/')

    container = WebDriverWait(driver , config.WAIT).until(EC.presence_of_element_located((By.CLASS_NAME , 'list-iTt_Zp4a')))
    links = WebDriverWait(container , config.WAIT).until(EC.presence_of_all_elements_located((By.TAG_NAME , 'a')))
    
    for i , element in enumerate(links):
        link = element.get_attribute('href')
        all_links.append(link)
        if i == 6:
            break
    driver.close()
    return all_links
