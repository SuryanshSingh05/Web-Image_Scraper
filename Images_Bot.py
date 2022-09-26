from turtle import delay
from selenium import webdriver      # webscraping lib
from selenium.webdriver.common.keys import Keys
import time 
search = input("What search do you want for the image to be downlaoded?")
num = int(input("How many images do you want to download, enter the number (recommended enter 5 more than you need)"))
num += 30
global driver
driver = webdriver.Chrome("C:\Dev\Python_Learning\chromedriver.exe")
driver.maximize_window()
 
driver.get('https://www.google.com/')
search_box = driver.find_element("xpath",'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys(search)
search_box.send_keys(Keys.ENTER) 

driver.find_element("xpath", '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_css_selector(".YstHxe input").click()
        time.sleep(3)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

    for i in range(30,num):
        try:
            driver.find_element("xpath", '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('C:\Dev\image-downloads\('+search+') ('+str(i-29)+').png')
            time.sleep(0.2)
        except:
            continue
driver.close()

        