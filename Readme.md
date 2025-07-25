````
# 🧵 Multi-Threaded Client-Server System in Python

This project demonstrates a simple **M-PESA-like simulation** using **Python threads and socket programming**. A single client program uses **four threads** to access different services hosted on **four separate ports** by the server. Each service runs concurrently and performs a unique task.

---

## 🧠 Features

- Uses **4 threads** in the client to simulate simultaneous access to different services.
- Each server service runs on a **dedicated port** and performs a specific operation.
- Demonstrates use of **Python's `threading` and `socket` libraries**.
- Useful for understanding **multi-threading**, **I/O-bound concurrency**, and **network programming**.

---

## 🔧 Services Implemented

| Service     | Port  | Description                                 |
|-------------|-------|---------------------------------------------|
| `add`       | 6001  | Adds two numbers and returns the result.    |
| `fact`      | 6002  | Computes the factorial of a given number.   |
| `reverse`   | 6003  | Reverses the given string.                  |
| `upper`     | 6004  | Converts a string to uppercase.             |

---

## 📁 Project Structure

project-root/
├── servers.py # Contains all 4 threaded service handlers
├── client.py # Spawns 4 threads to interact with services
└── README.md # Documentation


---

## ▶️ How to Run

### 1. Start the Servers
Open a terminal and run:
```bash
python3 servers.py

This will start all 4 services concurrently on different ports.

### 2. Run the Client
In another terminal, run:
python3 client.py

You'll be prompted to input data for each of the 4 services. Each request runs in its own thread and interacts with the respective server service.
````
