from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    XX = browser.find_element_by_id("input_value")
    x = XX.text
    y = calc(int (x))


    # Вводим ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()