"""Подключение драйверов"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Инициализация драйвера
driver = webdriver.Chrome(executable_path='./chromedriver')

# инициализируем страницу с Heroku
driver.get("http://the-internet.herokuapp.com/dropdown")

# находим элемент по ID
element = driver.find_element_by_id("dropdown")

# создаем класс Select и задаем element как параметр
drp = Select(element)

# выделяем по видимому тексту
drp.select_by_visible_text("Option 1")

# считаем сколько опций и выводим в терминале
print(len(drp.options))

all_options = drp.options
for option in all_options:
    print(option.text)

# Закрываем сессию
driver.close()


