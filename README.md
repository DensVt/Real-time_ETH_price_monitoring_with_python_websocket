#Этот код устанавливает подключение к серверу Binance через WebSocket-соединение и получает информацию о цене Ethereum в формате K-line с интервалом в 1 минуту в режиме реального времени.

#Каждый раз, когда приходит новое сообщение от сервера, функция on_message преобразует его в формат словаря Python и извлекает из него информацию о времени события и изменении цены в процентах. Если изменение цены за последний час равно или больше 1%, функция выведет сообщение в консоль.
#Функции on_error и on_close вызываются в случае ошибки или закрытия соединения соответственно, а функция on_open вызывается при установке соединения и сообщает об этом в консоль.

#WebSocketApp - это класс, который представляет WebSocket-подключение, и он используется для обработки сообщений, которые получает приложение. Метод run_forever запускает бесконечный цикл обработки сообщений

