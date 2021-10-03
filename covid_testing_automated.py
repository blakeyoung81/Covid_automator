from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium
import pickle
import csv

def wait_for_element(string, delay):
    wait = WebDriverWait(chrome, delay)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, string)))
    except TimeoutException:
        print ("Loading took too much time!")
    
def wait_and_click(xpath):
    wait_for_element(xpath,10)
    xpath = chrome.find_element_by_xpath(xpath)
    xpath.click()

def login_to_color(username, password,d_text,c_text):
    # login to Harvard
    url = "https://home.color.com/sign-in?next=%2Fcovid%2Factivation"
    chrome.get(url)
    wait_for_element('//*[@id="email-id"]',10)
    email = chrome.find_element_by_xpath('//*[@id="email-id"]')
    email.send_keys(username)
    passwordField = email = chrome.find_element_by_xpath('//*[@id="password-id"]')
    passwordField.send_keys(password)
    passwordField.send_keys(Keys.TAB)
    passwordField.send_keys(Keys.ENTER)
    print("enter has been pushed")

    activate = '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div/div/div/a'
    start_survey = '//*[@id="root"]/div/div/div[3]/div/a/span'
    no = '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/button'
    cont = '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/button/span/span/span/span'
    not_apply = '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[4]/button/p/span'
    cont2 = '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/button'
    term1 = '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[4]/label/span[1]/span[1]/input'
    term2 = '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[5]/label/span[1]/span[1]/input'
    term3 = '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[6]/label/span[1]/span[1]/input'
    term4 = '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[7]/label/span[1]/span[1]/input'
    cont3 = '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/a'
    cont4 = '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/form/div[9]/button/span/span/span/span'
    cont5 = '/html/body/div[3]/div[3]/div/div[3]/button[2]/span'
    d = '//*[@id="CovidBarcodeField"]'
    c = '//*[@id="AccessionNumberField"]'
    cont6 = '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/form/div[3]/button'
    cont7 = '/html/body/div[3]/div[3]/div/div[3]/button[2]/span'

    wait_and_click(activate)
    wait_and_click(start_survey)
    wait_and_click(no)
    wait_and_click(cont)
    wait_and_click(not_apply)
    wait_and_click(cont2)
    wait_and_click(term1)
    wait_and_click(term2)
    wait_and_click(term3)
    wait_and_click(term4)
    wait_and_click(cont3)
    wait_and_click(cont4)
    wait_and_click(cont5)
    wait_for_element(d,10)
    d_field = chrome.find_element_by_xpath(d)
    d_field.send_keys(d_text)
    d_field.send_keys(Keys.TAB)
    c_field = chrome.find_element_by_xpath(c)
    c_field.send_keys(c_text)
    wait_and_click(cont6)
    wait_and_click(cont7)

if __name__ == "__main__":
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    #change these values
    d_text = '1234567890'
    c_text = '12345'
    #change these values
    login_to_color("username", "password",d_text,c_text)
    # !!!! This program only works if you have an account and have uploaded the information of your account
    # You could edit that into the code though if you'd like






