import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")

driver = webdriver.Chrome(chromedriver_path)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://world-ships.com/")

flag_select = Select(driver.find_element_by_name("Ship[flag]"))
flag_select.select_by_value("218")

search_button = driver.find_element_by_name("yt0")
search_button.click()

try:
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.empty"))
    )
except Exception:
    pass

for row in driver.find_elements_by_css_selector("tr"):
    for cell in row.find_elements_by_tag_name("td"):
        print(cell.text)


driver.quit()
