Скрипт обладает следующим функционалом:
1. Получение данных из документа при помощи Google API, сделанного в Google Sheets.
2. Данные должны добавляться в БД, в том же виде, что и в файле–источнике, с добавлением колонки «стоимость в руб.»

    a. СУБД на основе PostgreSQL.

    b. Данные для перевода $ в рубли получаются по курсу ЦБ РФ.

3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме с настраиваемой частотой обновления

Дополнительно решение было упаковано в отдельные докер-контейнеры для базы данных и самого приложения, которые поднимаюися с помощью docker-compose. Осуществляется рассылка в тг-канал.
На выполнение всего ушло три часа.

Конфигурация и запуск приложения

Для запуска приложения необходимо поместить в директорию src/db_redactor json-файл с данными сервисного аккаунта "creds_google.json", полученный от сервисного аккаунта google api (возможно потребуется переименовать после загрузки)

Далее приложение можно поднять при помощи команды docker-compose up --build в корне проекта

Конфигурацию приложения можно осуществить с помощью src/db_redactor/config.py.
