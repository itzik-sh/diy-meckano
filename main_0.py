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
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

conf = webdriver.ChromeOptions()
conf.headless = True -1
# driver = webdriver.Chrome(ChromeDriverManager().install())
check_out_indication_ws_full_xpath = '/html/body/div[6]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/a/div[2]'
check_out_indication_ws_xpath = '//*[@id="checkout-button"]/div[2]'
check_out_indication_ws_selector = 'checkout-button > div.textOut'
check_in_time_ws_xpath = '//*[@id="organizer"]/div[2]/div/div[3]/div/div'
driver = webdriver.Chrome(PATH, options = conf)
driver.get("https://app.meckano.co.il/login.php#login")
print(driver.current_url)
time.sleep(3)
print("\tweb title: ", driver.title)
login_email_ws = driver.find_element_by_xpath('//*[@id="email"]')
login_pass_ws = driver.find_element_by_xpath('//*[@id="password"]')

login_email_ws.send_keys("itzik.sherf@devalore.com")
login_pass_ws.send_keys("asu5umu")
login_pass_ws.send_keys(Keys.RETURN)
print("going to sleep")
time.sleep(20)
print("waking up")


try:
    driver.find_element_by_css_selector("input[class='inputCheckInOut replace-to-checkin']")
    print("you're checked in")
    check_in_time_ws = driver.find_element_by_xpath('//*[@id="organizer"]/div[2]/div/div[3]/div/div').text
    print("Clock-in at ",check_in_time_ws[-5:])
except:
    try:
        driver.find_element_by_css_selector("input[class='inputCheckInOut replace-to-checkout']")
        print("you're checked out")
    except:
        print("did not manage to scarp checkin/out status")

