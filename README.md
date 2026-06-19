# Huawei Legacy SSH Connector

SSH коннектор для работы со **старой версии прошивки Huawei** (например MA5800-X2).

---

## Почему кастомный класс?

По умолчанию Netmiko во время `session_preparation` отправляет команду `screen-length 0 temporary`, чтобы отключить постраничный вывод.

На старой версии прошивки оборудовании Huawei эта команда **не существует**, из-за чего соединение падает с ошибкой:

```
MA5800-X2>screen-length0temporary
          ^
  % Unknown command, the error locates at '^'
```

Для решения был создан класс `HuaweiNoPagging`, который наследует `HuaweiSSH` и переопределяет `session_preparation` — убирает проблемную проверку, после чего соединение устанавливается корректно.

---

## Использование

```
python ssh_connector.py
```

Скрипт запросит:
- IP адрес устройства
- Username устройства
- Пароль

---

## Зависимости

```
pip install netmiko
```
