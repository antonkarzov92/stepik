from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_id("button")

    time.sleep(2240)
    browser.find_element_by_id("button")




    button = browser.find_element_by_tag_name("button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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