import platform
from subprocess import call

def anonymize_host():
    system = platform.system().lower()
    if "linux" not in system:
        print("⚠️ Anonymization only fully supported on Linux.")
        return

    try:
        print("👻 Anonymizing system...")
        call("iptables -F", shell=True)
        call("history -c", shell=True)
        call("rm -rf ~/.bash_history", shell=True)
        call("macchanger -r eth0", shell=True)
        call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
        call("echo 0 > /proc/sys/kernel/randomize_va_space", shell=True)
        print("✅ System anonymized.")
    except Exception as e:
        print(f"❌ Anonymization error: {e}")
