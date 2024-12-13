import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """Перевіряє, чи порт відкритий."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Таймаут для підключення
            s.connect((host, port))
            return port  # Якщо порт відкритий, повертаємо його номер
    except (socket.timeout, socket.error):
        return None  # Якщо порт закритий, повертаємо None

def main():
    print("Простий сканер портів")
    host = input("Введіть хост (IP або домен): ")
    start_port = int(input("Початковий порт: "))
    end_port = int(input("Кінцевий порт: "))

    print(f"Сканування портів з {start_port} по {end_port} на хості {host}...")

    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)

    if open_ports:
        print("Відкриті порти:")
        for port in open_ports:
            print(f"- {port}")
    else:
        print("Відкритих портів не знайдено.")

if __name__ == "__main__":
    main()

