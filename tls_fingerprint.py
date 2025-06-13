import random

def get_random_tls_headers():
    ja3_variants = [
        "771,4865-4866-4867-49195-49199-49196,0-10-11-13,23-24-25,0",
        "771,4865-49196-49195-49200-49199,0-11-10,23-24-25-29,0",
        "771,49195-49196-49199-49200,0-10-11-13-35,23-24-27-29,0",
        "771,4866-49199-49196,0-10-11-13-16,23-24,0"
    ]
    ja3_hash = random.choice(ja3_variants)

    headers = {
        "X-JA3-Fingerprint": ja3_hash,
        "X-TLS-Client": f"Chrome/{random.randint(90,120)}.0.{random.randint(1000,9999)}.100",
        "X-SSL-Emulation": "TLSv1.3"
    }
    return headers
