from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))

    button=browser.find_element_by_id("book")
    button.click()
 

    XX = browser.find_element_by_id("input_value")
    x = XX.text
    y = calc(int (x))


    # Вводим ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))

    button = browser.find_element_by_id("solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()