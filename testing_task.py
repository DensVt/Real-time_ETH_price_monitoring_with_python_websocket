import websocket
import json

# Функция для обработки сообщения
def on_message(ws, message):
    # Преобразование из json в словарь Python
    data = json.loads(message)
    price = float(data['k']['c'])
    print(f"Price: {price}")
    
    prices.append(price)
    if len(prices) > 60:
        prices.pop(0)
        
    if (max(prices) - min(prices))/min(prices) > 0.01:
        print("Цена изменилась более чем на 1% за последние 60 минут")

# Функция для обработки ошибки
def on_error(ws, error):
    print(error)

# Функци для обработки закрытия соединения
def on_close(ws):
    print("### closed ###")

# функция для отправки запроса на сервер
def on_open(ws):
    print("### opened ###")


if __name__ == "__main__":
    prices = []
    # создаем экземпляр класса WebSocket и передаем туда ф-ции для обработки сообщений, ошибок и закрытия соединения
    ws = websocket.WebSocketApp("wss://fstream.binance.com/ws/ethusdt@kline_1m",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    # запуск бесконечного цикла для обработки сообщений
    ws.run_forever()
