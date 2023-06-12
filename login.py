# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-certificate-errors')
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver = webdriver.Chrome(options=options, executable_path='/home/vsts/work/1/drop-perftests/chromedriver')
    driver.get('https://www.saucedemo.com/')

login('standard_user', 'secret_sauce')

