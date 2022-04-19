from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"
driver = webdriver.Chrome(r"C:\PyCharmProjects\vildan\скрапинг))\chromedriver\chromedriver.exe")
driver.get(url)
data_list = []

try:
    buttons = driver.find_elements(By.XPATH, "//button[@class='btn btn-default page']")
    for page, i_button in enumerate(buttons):
        elements = driver.find_elements(By.XPATH, "//div[@class='caption']")
        for i_elem in elements:
            current_elem = i_elem.text.split('\n')
            data_list.append({'price': current_elem[0], 'description': current_elem[2]})
        driver.execute_script("arguments[0].click();", i_button)
        time.sleep(0.5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

for i_elem in data_list:
    print(f'Описание товара: {i_elem.get("description")}\nЦена: {i_elem.get("price")}')
    print()
