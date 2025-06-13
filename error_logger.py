import traceback

ramlog = []

def log_error(e):
    ramlog.append(traceback.format_exc())

def show_log():
    if ramlog:
        print("📄 In-Memory Error Log:")
        for line in ramlog:
            print(line)
    else:
        print("✅ No runtime errors captured.")
