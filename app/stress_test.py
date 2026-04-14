import requests
import time
import threading

URL = "https://your-app.onrender.com/generate"

payload = {
    "topic": "AI in gaming"
}

def send_request(i):
    try:
        res = requests.post(URL, params=payload)
        print(f"Request {i}: {res.status_code}")
    except Exception as e:
        print(f"Request {i}: ERROR {e}")

threads = []

# 🔥 20 concurrent requests
for i in range(20):
    t = threading.Thread(target=send_request, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
