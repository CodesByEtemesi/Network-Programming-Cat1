import socket
import threading
import time


def handle_client(conn, addr):
    print(f"Connected by {addr}")
    conn.send(b"Select service:\n1. Celsius to Fahrenheit\n2. Prime Check\n3. Current Time\n4. Reverse a String\nEnter choice (1-4): ")
    choice = conn.recv(1024).decode()

    if choice == '1':
        conn.send(b"Enter temperature in Celsius: ")
        celsius = float(conn.recv(1024).decode())
        fahrenheit = (celsius * 9/5) + 32
        conn.send(f"{celsius}°C = {fahrenheit}°F".encode())

    elif choice == '2':
        conn.send(b"Enter number to check for prime: ")
        num = int(conn.recv(1024).decode())
        if num < 2:
            result = f"{num} is not a prime number."
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    result = f"{num} is not a prime number."
                    break
            else:
                result = f"{num} is a prime number."
        conn.send(result.encode())

    elif choice == '3':
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        conn.send(f"Current server time: {current_time}".encode())

    elif choice == '4':
        conn.send(b"Enter a string to reverse: ")
        text = conn.recv(1024).decode()
        conn.send(f"Reversed: {text[::-1]}".encode())

    else:
        conn.send(b"Invalid choice.")

    conn.close()


def main():
    host = 'localhost'
    port = 5050
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server running on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


main()
