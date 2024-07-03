from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
import pandas as pd
from io import StringIO
import time

driver = webdriver.Chrome()
driver.get("https://voterlist.election.gov.np/bbvrs1/index_2.php")

df = pd.DataFrame()

def select_dropdown_by_index(selector, index):
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, selector))
    )
    Select(dropdown).select_by_index(index)
    time.sleep(0.2)# necessary if page needs some time to react to the dropdown change

def scraper():
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find('table', class_='bbvrs_data dataTable')
    converters = {'मतदाता नं': str}
    data = pd.read_html(StringIO(str(table)), converters=converters)[0]
    return data

def post_submit_actions():
    entries_dropdown = driver.find_element(By.XPATH, '//select[@name="tbl_data_length"]')
    Select(entries_dropdown).select_by_value("100")

    while True:
        new_data = scraper()
        global df
        df = pd.concat([df, new_data], ignore_index=True)
        try:
            next_page_link = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "paginate_enabled_next"))
            )
            driver.execute_script("arguments[0].click();", next_page_link)
        except:
            print("No more pages available")
            break

try:
    for state_index in range(7, 8):
        try:
            for dist_index in range(9, 10):
                try:
                    for mun_index in range(1, 14):
                        try:
                            for ward_index in range(1, 20):
                                try:
                                    for reg_centre_index in range(1, 5):
                                        try:
                                            select_dropdown_by_index('//select[@id="state"]', state_index)
                                            select_dropdown_by_index('//select[@id="district"]', dist_index)
                                            select_dropdown_by_index('//select[@id="vdc_mun"]', mun_index)
                                            select_dropdown_by_index('//select[@id="ward"]', ward_index)
                                            select_dropdown_by_index('//select[@id="reg_centre"]' ,reg_centre_index)
                                            submit_button = driver.find_element(By.ID, "btnSubmit")
                                            submit_button.click()
                                            post_submit_actions()
                                            go_back = driver.find_element(By.CLASS_NAME, "a_back")
                                            go_back.click()
                                        except NoSuchElementException:
                                            break
                                except NoSuchElementException:
                                    break
                        except NoSuchElementException:
                            break
                except NoSuchElementException:
                    break
        except NoSuchElementException:
            break
except Exception as e:
    print("An error occurred:", str(e))
finally:
    driver.quit()

df.to_csv('Baitadi_Voters.csv')