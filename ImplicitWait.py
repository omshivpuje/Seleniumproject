# Waits
# Implicit wait
# Explicit wait

from LaunchDriver import Browser

browser = Browser()
browser.driver.implicitly_wait(10)    # We can specify the implicit wait only one time
# Implicit wait is used to wait until the components are loaded within provided wait time
