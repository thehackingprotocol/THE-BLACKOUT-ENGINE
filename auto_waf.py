import requests

def scan_waf(target):
    print(f"🔍 Scanning WAF for: {target}")
    try:
        r = requests.get(target, timeout=5)
        headers = r.headers

        wafs = {
            "cloudflare": ["cf-ray", "cf-cache-status"],
            "akamai": ["akamai-", "aka-"],
            "aws": ["x-amzn", "x-amz-cf-"],
            "imperva": ["x-iinfo", "x-cdn"],
            "incapsula": ["x-cdn", "visid_incap_"],
            "sucuri": ["x-sucuri-id"],
            "fastly": ["x-fastly-request-id"]
        }

        detected = []
        for waf, indicators in wafs.items():
            for i in indicators:
                for h in headers:
                    if i.lower() in h.lower() or i.lower() in headers[h].lower():
                        detected.append(waf.upper())

        if detected:
            print(f"🛡️ WAF Detected: {', '.join(set(detected))}")
        else:
            print("✅ No WAF fingerprint found (not guaranteed)")
    except Exception as e:
        print(f"❌ WAF scan error: {str(e)}")
