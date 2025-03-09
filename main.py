import os
from dotenv import load_dotenv
import uuid
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template

# app = Flask(__name__)

addresses = [
    "1234 Main St, Springfield, IL 62701",
    "1600 Pennsylvania Ave NW, Washington, DC 20500",
    "221B Baker St, London NW1 6XE, United Kingdom",
]

# @app.route("/beans")
def index():
    load_dotenv()
    # chrome_options = Options()
    # # chrome_options.add_argument("--headless")  
    # chrome_options.add_argument("--no-sandbox")  
    # # chrome_options.add_argument("--disable dev-shm-usage")  
    # chrome_options.add_argument('--window-size=1920,1080') 
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    # chrome_options.add_argument('user-agent={0}'.format(user_agent))

    unique_id = str(uuid.uuid4())
    driver = webdriver.Chrome()
    assert driver


    driver.get('https://www.google.com/maps')
    saved_tab = driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[1]/ul/li[2]/button/div[1]/span")
    saved_tab.click()

    email_form = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
    )


    email_form.send_keys(os.getenv("EMAIL"))
    sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button")
    old_url = driver.current_url
    sign_in_button.click()



    WebDriverWait(driver, 10).until(EC.url_changes(old_url))
    time.sleep(2)
    password_form = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))
    )
    password_form.send_keys(os.getenv("PASSWORD"))
    password_button = driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button")
    old_url = driver.current_url
    password_button.click()

    WebDriverWait(driver, 10).until(EC.url_changes(old_url))


    driver.get('https://www.google.com/maps')


    old_url = driver.current_url
    WebDriverWait(driver, 10).until(EC.url_changes(old_url))
    saved_tab = driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[1]/ul/li[2]/button/div[1]/span")
    saved_tab.click()

    newlistbutton1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'BgrMEd')]//span[contains(text(), 'New list')]")))
    newlistbutton1.click()



    list_form = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"//input[@aria-label='List name']")))
    list_form.send_keys(unique_id)



    list_form_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='modal-dialog']/div/div[2]/div/div[2]/div/div/div[4]/div[2]/button")))
    list_form_button.click()

    time.sleep(20)
    # list made
    for address in addresses:
        for char in address:
            if char == ",":
                address = address.replace(char, "%2C")
            if char == " ":
                address = address.replace(char, "%20")
        
        driver.get('https://www.google.com/maps/search/?api=1&query=' + address)
        driver.implicitly_wait(3)
        save_button1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//button[contains(@class, 'g88MCb')]//div[contains(text(), 'Save')]")))
        save_button1.click()
        list_buttom = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((By.XPATH,f"//div[//*[@id='action-menu']]//div[contains(text(), '{unique_id}')]")))
        try:
            list_buttom.click()
        except:
            driver.execute_script("arguments[0].click();", list_buttom)
        time.sleep(5)
    newlistbutton1.click()
    time.sleep(100)
    driver.quit()

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)


def create_list(addresses):
    load_dotenv()
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")  
    # chrome_options.add_argument("--disable dev-shm-usage")  
    chrome_options.add_argument('--window-size=1920,1080') 
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    chrome_options.add_argument('user-agent={0}'.format(user_agent))

    unique_id = str(uuid.uuid4())
    driver = webdriver.Chrome(options= chrome_options, service=Service(ChromeDriverManager().install()))
    assert driver


    driver.get('https://www.google.com/maps')
    saved_tab = driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[1]/ul/li[2]/button/div[1]/span")
    saved_tab.click()

    email_form = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
    )


    email_form.send_keys(os.getenv("EMAIL"))
    sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button")
    old_url = driver.current_url
    sign_in_button.click()



    WebDriverWait(driver, 10).until(EC.url_changes(old_url))
    time.sleep(2)
    password_form = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))
    )
    password_form.send_keys(os.getenv("PASSWORD"))
    password_button = driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button")
    old_url = driver.current_url
    password_button.click()

    WebDriverWait(driver, 10).until(EC.url_changes(old_url))


    driver.get('https://www.google.com/maps')


    old_url = driver.current_url
    WebDriverWait(driver, 10).until(EC.url_changes(old_url))
    saved_tab = driver.find_element(By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[1]/ul/li[2]/button/div[1]/span")
    saved_tab.click()

    newlistbutton1 = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'BgrMEd')]//span[contains(text(), 'New list')]")))
    newlistbutton1.click()



    list_form = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH,"//input[@aria-label='List name']")))
    list_form.send_keys(unique_id)



    list_form_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='modal-dialog']/div/div[2]/div/div[2]/div/div/div[4]/div[2]/button")))
    list_form_button.click()
    time.sleep(2)
    back_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH,"//button[contains(@class, 'hYBOP')]")))
    back_button.click()

    menu_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div/button")))
    menu_button.click()

    share_options = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH,"//div[//*[@id='action-menu']]//div[contains(text(), 'Sharing options')]")))
    try:
        share_options.click()
    except:
        driver.execute_script("arguments[0].click();", share_options)

    share_radio = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/div/div/div[3]/div[3]/div/input")))
    try:
        share_radio.click()
    except:
        driver.execute_script("arguments[0].click();", share_radio)
    
    share_button = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/div/div/div[3]/div[5]/button/span/span[2]")))
    try:
        share_button.click()
    except:
        driver.execute_script("arguments[0].click();", share_button)

    list_box = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/input")))
    list_text = list_box.get_attribute("value")
    time.sleep(5)
    # list made
    for address in addresses:
        for char in address:
            if char == ",":
                address = address.replace(char, "%2C")
            if char == " ":
                address = address.replace(char, "%20")
        
        driver.get('https://www.google.com/maps/search/?api=1&query=' + address)
        driver.implicitly_wait(3)
        save_button1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//button[contains(@class, 'g88MCb')]//div[contains(text(), 'Save')]")))
        save_button1.click()
        list_buttom = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,f"//div[//*[@id='action-menu']]//div[contains(text(), '{unique_id}')]")))
        try:
            list_buttom.click()
        except:
            driver.execute_script("arguments[0].click();", list_buttom)
        time.sleep(5)
    print(list_text)
    driver.quit()

create_list(addresses)