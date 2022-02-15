"""Подключение драйверов"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""Инициализация драйвера
1. Даем команду инициализировать страницу с Heroku.
2. Находим через dev tools элементы username&password и методом send_keys пишем в username-tomsmith и password-SuperSecretPassword!
3. Находим элемент по xpath
4. Запускаем код
"""
driver = webdriver.Chrome(
    executable_path='./chromedriver'
)

driver.get("http://the-internet.herokuapp.com/login")
driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
driver.find_element_by_xpath("//*[@id='login']/button/i").click()

# Проверяем, присутствует ли этот текст на странице
assert "You logged into a secure area!" in driver.page_source

# Закрываем сессию
driver.close()








