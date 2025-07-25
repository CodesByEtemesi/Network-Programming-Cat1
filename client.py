import socket


def main():
    host = 'localhost'
    port = 5050

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Display menu
        menu = s.recv(1024).decode()
        print(menu)
        choice = input("Your choice: ")
        s.send(choice.encode())

        if choice in ['1', '2', '4']:
            prompt = s.recv(1024).decode()
            value = input(prompt)
            s.send(value.encode())

        result = s.recv(1024).decode()
        print("Result:", result)


main()
