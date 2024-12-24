import re

def is_valid_ipv4(ip: str) -> bool:
    pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
    if pattern.match(ip):
        parts = ip.split(".")
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

def get_valid_ipv4(ip: str) -> str:
    if is_valid_ipv4(ip):
        return ip
    else:
        raise ValueError(f"Некорректный IPv4-адрес: {ip}")

print(is_valid_ipv4("192.168.1.1"))  # True
print(is_valid_ipv4("256.256.256.256"))  # False

try:
    print(get_valid_ipv4("192.168.1.1"))  # "192.168.1.1"
    print(get_valid_ipv4("256.256.256.256"))  # ValueError
except ValueError as e:
    print(e)
