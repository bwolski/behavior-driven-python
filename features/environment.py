"""
This module contains environment controls:
http://behave.readthedocs.io/en/latest/api.html#environment-file-functions
The functions handle Selenium WebDriver setup and cleanup.
(Alternatively, fixtures could be used: http://behave.readthedocs.io/en/latest/fixtures.html)
"""

from selenium import webdriver


# Hooks

# Firefox is the hard-coded browser of choice.
# Feel free to change it here.
# The correct browser and WebDriver executable must be installed on the test machine.
# A flexible framework would read the browser choice from inputs or config data.

SAUCE_USERNAME = 'ben_wolski'
SAUCE_ACCESS_KEY = 'ca8ed953-f7fa-458e-a2f3-2f791cc147a3'

def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser = webdriver.Remote(
            desired_capabilities = webdriver.DesiredCapabilities.FIREFOX, 
              command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' 
                % (SAUCE_USERNAME, SAUCE_ACCESS_KEY))
        context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
