# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = 'https://c0bf1796-6054-4f26-8c6a-b11c3465b3bf.serverhub.praktikum-services.ru'

# DOC_PATH содержит путь к документации веб-сервиса.
# Этот путь используется для формирования полного URL пути к документации, добавляя его к базовому URL сервиса.
# В результате получится что-то вроде "https://api.example.com/docs/"
DOC_PATH = '/docs/'
CREATE_ORDER = "/api/v1/orders"
GET_ORDER_DETAILS = "/api/v1/orders/track"