import time

from selenium import webdriver

# Set the webdriver.opera.driver environment variable
webdriver.opera.driver = "/path/to/operadriver"

# Create a new Selenium WebDriver instance using the OperaDriver class
driver = webdriver.OperaDriver()

# Open the Google homepage
driver.get("https://www.google.com/")

# Wait for the page to load
time.sleep(5)

# Quit the browser
driver.quit()
