# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data

def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


# Определяем функцию post_orders, которая отправляет POST-запрос к серверу для получения логов
def post_orders(body):
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения POST-запроса
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json = body,
                         headers = data.headers)


def get_orders_details(track):
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения POST-запроса
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_DETAILS + "?t=" + str(track),
                        headers = data.headers)
