# Импортируем библиотеку requests для создания Get и Post запроса
import requests

# Ссылка на файл который надо скачать
link = 'http://the-internet.herokuapp.com/download/TextDoc.txt'

# Создаем функцию который будет генерировать нам имя и скачивать в текущую директорию
def save_from_url(link):
    filename = link.split('/')[-1] # Берем линк и разбиваем его методом сплит и берем последнее значение
    print(filename)
    r = requests.get(link, allow_redirects=True) # тут мы получаем контент по этой ссылке, а также прописываем, что мы можем быть перенправлены
    open(filename, "wb").write(r.content) # Открываем файл на запись и записываем туда контент который мы получили из этого запроса

save_from_url(link)

# с помощью readline вывожу что наход-ся в файле
file = open("TextDoc.txt")
print(file.readline())
file.close()