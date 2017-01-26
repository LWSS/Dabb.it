import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get("https://facebook.com")
raw_input("Log into Facebook. Then press [Enter]")


rabbitUrl = "https://www.rabb.it/xxxxxx"


def visit( ):
    driver.get(rabbitUrl);
    while True:
        try:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toolbarButton signInButton']")))
            except TimeoutException:
                print "Signin button is not clickable."
                quit()
            signinBtn = driver.find_element_by_xpath("//div[@class='toolbarButton signInButton']")
            signinBtn.click()
            facebookBtn = driver.find_element_by_xpath("//*[@id=\"rabbitapp\"]/div[10]/div[1]/form/div[3]/div/a")
            facebookBtn.click()
            break
        except WebDriverException:
            print "Waiting to SignIn..."

    while True:
        try:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"rabbitapp\"]/div[10]/div[1]/form/div[3]/div/a")))
            except TimeoutException:
                print "Facebook button is not clickable."
                quit()
            facebookBtn = driver.find_element_by_xpath("//*[@id=\"rabbitapp\"]/div[10]/div[1]/form/div[3]/div/a")
            facebookBtn.click()
            break
        except WebDriverException:
            print "Waiting to Facebook Login..."

    while True:
        try:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"rabbitapp\"]/div[10]/div[2]/button[1]")))
            except TimeoutException:
                print "Stay Here Button not clickable"
                quit()
            stayBtn = driver.find_element_by_xpath("//*[@id=\"rabbitapp\"]/div[10]/div[2]/button[1]")
            stayBtn.click()
            break
        except WebDriverException:
            print "Waiting to StayHere..."
            
       
    return

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    

def reset( ):
    while True:
        try:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"rabbitapp\"]/div[4]/div/div[2]/div[4]/div[1]/div[2]")))
            except TimeoutException:
                print "Arrow for signOut Not Clickable"
                quit()
            arrow = driver.find_element_by_xpath("//*[@id=\"rabbitapp\"]/div[4]/div/div[2]/div[4]/div[1]/div[2]")
            arrow.click()
            break
        except WebDriverException:
            print "Waiting to Arrow..."
            
    while True:
        try:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"rabbitapp\"]/div[4]/div/div[2]/div[4]/div[2]/div/div[3]")))
            except TimeoutException:
                print "Signout Not Clickable"
                quit()
            signoutBtn = driver.find_element_by_xpath("//*[@id=\"rabbitapp\"]/div[4]/div/div[2]/div[4]/div[2]/div/div[3]")
            signoutBtn.click()
            break
        except WebDriverException:
            print "Waiting to SignOut..."
            
    return;
visit()
while True:
    if check_exists_by_xpath( "//*[@id=\"rabbitapp\"]/div[2]/div[1]/div/div[2]/div/h1" ):
        reset()
        time.sleep(0.5)
        visit()
    time.sleep(0.1)
