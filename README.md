# Huawei Legacy SSH Connector

SSH коннектор для работы со **старым оборудованием Huawei** (например MA5800-X2).

---

## Почему кастомный класс?

По умолчанию Netmiko во время `session_preparation` отправляет команду `screen-length 0 temporary`, чтобы отключить постраничный вывод.

На старом оборудовании Huawei эта команда **не существует**, из-за чего соединение падает с ошибкой:

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
- Пароль (username захардкожен как `root`)

---

## Зависимости

```
pip install netmiko
```
