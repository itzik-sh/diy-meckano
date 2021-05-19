# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
# from selenium import webdriver
# driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
# driver.get('http://inventwithpython.com')
# opts = Options()
# opts.set_headless()
# assert opts.headless  # Operating in headless mode
# browser = Firefox(options=opts)
# browser.get('https://duckduckgo.com')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://app.meckano.co.il/login.php#login")
print(driver.current_url)
# login_email_ws_xpath = //*[@id="email"]
check_in_time_ws_xpath = '//*[@id="organizer"]/div[2]/div/div[3]/div/div'
# login_email_ws = driver.find_element_by_class_name("email input-text-email")
login_email_ws = driver.find_element_by_xpath('//*[@id="email"]')
login_pass_ws = driver.find_element_by_xpath('//*[@id="password"]')

login_email_ws.send_keys("itzik.sherf@devalore.com")
login_pass_ws.send_keys("asu5umu")
login_pass_ws.send_keys(Keys.RETURN)
print("going to sleep")
time.sleep(20)
print("waking up")
print(driver.current_url)
print("getting")
print(driver.current_url)
check_in_status_ws = driver.find_element_by_xpath(check_in_time_ws_xpath)
print(check_in_status_ws)
print("scrapped")
info = check_in_status_ws.get_attribute('innerHTML')
print(info)
