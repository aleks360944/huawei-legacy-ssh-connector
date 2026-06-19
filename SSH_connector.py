import getpass
from netmiko.huawei.huawei import HuaweiSSH
from netmiko import (NetmikoTimeoutException, NetmikoAuthenticationException)
from time import sleep

class HuaweiNoPagging(HuaweiSSH):
    def session_preparation(self):
        self._test_channel_read()
        return super().session_preparation()
 
def search_index(output_text):
    for line in output_text.splitlines():
        if "Next valid free service virtual port ID" in line:
            parts = line.split(":")
            index = parts[1].strip()
            return index   
    return None
     

print("Данный SSH_Connector работает со старой версии прошивки оборудования huawei\n\n")        
host = input("Введите IP Адрес: ")
username = input("Введите username: ").strip()
password = getpass.getpass("Введите пароль: ")

conn = None

try:
    conn = HuaweiNoPagging(
        host=host,
        username="root",
        password=password
    )

    print(f"Успешно подключились к {host}")

    conn.write_channel("enable\n\n")
    sleep(0.5)

    conn.write_channel("config\n\n")
    sleep(0.5)

    conn.write_channel("display service-port next-free-index\n\n")
    sleep(1)

    output = conn.read_channel()

    index = search_index(output)
    print(f"Next free index is: {index}")
    
except NetmikoTimeoutException:
    print(f"\nХост {host} недоступен или не отвечает")
    print("Проверьте правильность ввода")
    
except NetmikoAuthenticationException:
    print(f"\nОшибка авторизации на хост {host}")
    
except Exception as e:
    print(f"\nОшибка {e}, попробуйте снова")
    
finally:
    if conn:
        try:
            conn.disconnect()
        except Exception:
            pass