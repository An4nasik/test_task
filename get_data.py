from requests import request, Response
from decouple import config


class CardReader:
    def __init__(self, url: str, method: str) -> None:
        self.url = url #url куда мы направляем запрос
        self.method = method #метод этого запроса

    def read_data(self, n: int, photo: bool = False) -> Response:
        api_key = {"Authorization": config("API_KEY")}
        # создается специальный параметр для запроса к товарам
        # он используется в моем предполагаемом методе получения данных
        cursor = {
            "settings": {
                "cursor": {
                    "limit": n
                },
                "filter": {
                    "withPhoto": photo
                }
            }
        }
        dt = request(self.method, self.url, headers=api_key, params=cursor)
        return dt

