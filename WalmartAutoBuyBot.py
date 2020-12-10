from config import keys
import time
from selenium import webdriver

def order(k):
    global driver
    isLoaded = False
    options = webdriver.ChromeOptions() 

    options.add_argument("user-data-dir=" + k['chrome_profile'])
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    #print(driver.execute_script("return navigator.userAgent;"))
    driver.get(k['product_url'])

    time.sleep(3)
    
    try:
        # cookie close button
        driver.find_element_by_xpath('//*[@id="accept-privacy-policies"]').click()
        time.sleep(1)
    except: pass
    finally:
        while isLoaded is False:
            try:
                # add to cart button
                driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div[3]/div[2]/div/div[2]/div[2]/div/button[1]').click()        
                isLoaded = True
                time.sleep(1.5)
            except: pass
        isLoaded = False

        while isLoaded is False:
            try:
                # checkout button
                driver.find_element_by_xpath('//*[@id="atc-root"]/div[3]/div[2]/button[1]').click()
                isLoaded = True
                time.sleep(1)
            except: pass
        isLoaded = False

        while isLoaded is False:
            try:
               #proceed to checkout button
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[4]/div[2]/div/div[1]/div[11]/a/button').click()
                isLoaded = True
                time.sleep(1.2)
            except: pass
        isLoaded = False

        while isLoaded is False:
            try:
                #place order button
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/button').click()
                isLoaded = True
            except: pass
             
if __name__ == '__main__':
    order(keys)