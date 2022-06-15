from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time 
# defining the webdriver and config btw this code will be almost the same in all of your selenium scripts
options = Options()

# !!! blocking browser notifications !!!
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)

# starting in maximized window
options.add_argument("start-maximized")
options.add_argument("--disable-default-apps")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://playtictactoe.org/")
lista = ["square top left" ,"square top" ,"square top right" ,"square left" ,"square" ,"square right" ,"square bottom left" ,"square bottom" ,"square bottom right" ]

# time.sleep(1)
# button = driver.find_element(By.CLASS_NAME, "scores")
# button.click()

# time.sleep(1)
# elem = driver.find_element(By.XPATH,"//div[@class='square top left']")
# elem.click()
# time.sleep(1)

# selected = lista[index]
# xpath = "//div[@class='"+selected+"']"
# elem = driver.find_element(By.XPATH,xpath)
# elem.click()

