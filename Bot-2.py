запросы на import
import json
из конфигурации import keys


класс ConvertionException(исключение):
    пройти


класс MoneyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        если цитата == база:
            raise ConvertionException(f'Невозможно конвертировать одинаковые валюты {base}.')

        попробуйте:
            quote_ticker = ключи[quote]
        кроме KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        попробуйте:
            base_ticker = ключи[база]
        кроме KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        попробуйте:
            сумма = float(сумма)
        кроме ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        возврат total_base * amount