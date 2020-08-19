import ExcelUtils
from LaunchDriver import Browser
from selenium.webdriver.common.by import By
import time

browser = Browser()
browser.get_url()

browser.driver.switch_to.frame("frame-one1434677811")

rows = ExcelUtils.get_rows_from_sheet()
columns = ExcelUtils.get_columns_from_sheet()

fn = browser.driver.find_element(By.ID, "RESULT_TextField-1")
ln = browser.driver.find_element(By.ID, "RESULT_TextField-2")
for r in range(2, rows+1):
    first_name = ExcelUtils.get_cell_value(r, 1)
    last_name = ExcelUtils.get_cell_value(r, 2)

    # Send the excel data to application
    fn.send_keys(first_name)
    ln.send_keys(last_name)

    # Write the data in excel
    ExcelUtils.write_cell_value(r, 3, "Write Success!")
    fn.clear()
    ln.clear()

time.sleep(5)
browser.close_browser()
