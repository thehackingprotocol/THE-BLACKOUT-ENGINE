import os
import sys
import time

def self_delete():
    try:
        file = sys.argv[0]
        print("💣 Self-deletion triggered. Shredding in 5 seconds...")
        time.sleep(5)
        os.remove(file)
        print("✅ Executable removed.")
    except Exception as e:
        print(f"❌ Failed to self-delete: {e}")
