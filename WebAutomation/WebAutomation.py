#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.chrome.options import Options
import glob
import os
import time
from os import path

#Get the current directory
current_dir=os.getcwd()
#Setup Webdriver download options
options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r''+current_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
#load webdriver for chrome
browser = webdriver.Chrome(options=options,executable_path=r'./chromedriver')

#open the website
browser.get ('http://www.rpachallenge.com/')
assert 'Rpa Challenge' in browser.title

start=browser.find_element_by_class_name('uiColorButton')
#down load the file
file=browser.get('http://www.rpachallenge.com/assets/downloadFiles/challenge.xlsx')

#Check if the file is downloaded
while not os.path.exists('challenge*.xlsx'):
    time.sleep(2)

if os.path.isfile('challenge.xlsx'):
    list_of_files = glob.glob('*.xlsx')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    df=pd.read_excel(latest_file)
    df.head()

    start.click()
    for ind in df.index:
        #Select the elements using CSS selector
        nextround=browser.find_element_by_css_selector('[value="Submit"]')
        labelFirstName = browser.find_element_by_css_selector(".ng-pristine[ng-reflect-name='labelFirstName']")
        labelLastName = browser.find_element_by_css_selector(".ng-pristine[ng-reflect-name='labelLastName']")
        labelAddress = browser.find_element_by_css_selector(".ng-pristine[ng-reflect-name='labelAddress']")
        labelEmail = browser.find_element_by_css_selector(".ng-pristine[ng-reflect-name='labelEmail']")
        labelRole = browser.find_element_by_css_selector(".ng-pristine[ng-reflect-name='labelRole']")
        labelPhone = browser.find_element_by_css_selector(".ng-pristine[ng-reflect-name='labelPhone']")
        labelCompanyName = browser.find_element_by_css_selector(".ng-pristine[ng-reflect-name='labelCompanyName']")

# Filling data fileds
        labelFirstName.send_keys(df['First Name'][ind])
        labelLastName.send_keys(df['Last Name '][ind])
        labelAddress.send_keys(df['Address'][ind])
        labelRole.send_keys(df['Role in Company'][ind])
        labelPhone.send_keys(str(df['Phone Number'][ind]))
        labelCompanyName.send_keys(df['Company Name'][ind])
        labelEmail.send_keys(df['Email'][ind])
        #Click submit
        nextround.click()

    message=browser.find_element_by_css_selector('[class="message2"]')
    #Create a file with the success rate

    f= open("congrats.txt","w+")
    f.write(message.text)
    f.close()



browser.close()