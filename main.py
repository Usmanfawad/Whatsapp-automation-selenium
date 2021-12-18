from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import winsound
import time

os.system("script.bat")
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options = opt)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
#Enter the target number in the target variable. Example +923335141414
target = "+923335141414"
string = "Testing whatsapp automation python"
x_arg = '//*[@id="side"]/div[1]/div/label/div/div[2]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
winsound.Beep(700, 800)
group_title.click()
group_title.send_keys(target+Keys.ENTER)
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
input_box.send_keys("Test successful" + Keys.ENTER)
time.sleep(4)
driver.close()
