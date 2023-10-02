from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)

# Now you can use the 'driver' object to interact with web pages.
