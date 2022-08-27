# In the light of TCM-Security going down, I have nothing better to do with my life, so here we are...
# Automate your life!
# Automatic timecard input to save time

# Selenium is required !! Do not forget to change the path to your chrome driver!

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

# File paths for Chromedriver and webdriver setup


#Variables
url = "MAINPAGEFORTIMESHEET"
username = input('What is your username?: ')
password = input('What is your super secret password?: ')

# Function for logging onto the website
def logonStep():
    # FIle paths for chrome driver setup. You can put these two lines outside the function
    # but the chrome localhost comes up which blocks the input for username and password
    # ddelement is used below in the script for dropdown element call which uses import select

    s = Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=s)


    #Navigation and sending user/pass to the web server
    driver.get(url)
    driver.find_element(by='xpath', value='//a[@href="(TIMESHEETSPLASHPAGEURL.REDACTED"]').click()
    time.sleep(2)
    driver.find_element(by='id', value="txtUser").send_keys(username)
    time.sleep(2)
    driver.find_element(by='id', value='txtPassword').send_keys(password)
    driver.find_element(by='id', value='btnLogin').click()
    time.sleep(1)
    # This try statement will accept the auto alert that pops up and prints the result whether it had one or not
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")
    time.sleep(3)

    # This will then navigate to the tab for timesheet input
    driver.find_element(by='xpath', value='//a[@href="XPATH OF TIMESHEET URL"]').click()
    driver.find_element(by='id', value='btnCreate').click()
    time.sleep(3)
    ddelement = Select(driver.find_element(by='id', value='ddlTaskOrders'))
    ddelement.select_by_index(1)
    driver.find_element(by='id', value='btnAdd').click()

    time.sleep(20)



def menu():
    if (username and password != ""):
        print("1. Create new timesheet and add 8 hours on Mon-Fri")
        print("2. Exit/Quit")
        options = input('What would you like to do?: ')
        if (options==("1")):
            print("Loading...", logonStep())

        elif (options==("2")):
            print("Logging out")
        elif (options!=("1" or "2")):
            print("Invalid option.", menu())


    else:
        print("Please enter valid logon credentials.")

menu()
