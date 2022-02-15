from selenium import webdriver

# Инициализация драйвера
driver = webdriver.Chrome(executable_path='./chromedriver')

# инициализируем страницу с Heroku
driver.get("http://the-internet.herokuapp.com/key_presses")

# находим элемент по ID и отправляем букву "а"
driver.find_element_by_id("target").send_keys("a")

# Закрываем браузер
driver.close()