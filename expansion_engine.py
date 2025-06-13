import random
from tls_fingerprint import get_random_tls_headers

def build_payload_headers(target, enable_expansions=True, http2=False):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (Windows NT 10.0; WOW64)"
        ]),
        "Referer": f"https://duckduckgo.com/?q={random.randint(1000,9999)}",
        "X-Forwarded-For": ".".join(str(random.randint(1, 255)) for _ in range(4)),
        "Connection": "keep-alive"
    }

    if enable_expansions:
        headers.update({
            "X-Cookie-Bomb": ";".join([f"SESSIONID{random.randint(1,999)}={random.randint(100000,999999)}" for _ in range(5)]),
            "Cache-Control": "no-store",
            "DNT": "1",
            "X-Fake-WAF": "Cloudflare-Bypass",
            "Upgrade-Insecure-Requests": "1"
        })
        headers.update(get_random_tls_headers())

    if http2:
        headers["X-Proto-Emulation"] = "HTTP/2"

    return headers
