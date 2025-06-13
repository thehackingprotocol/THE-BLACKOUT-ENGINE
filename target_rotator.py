def load_targets(single, list_path):
    targets = []

    if single and single.endswith(".txt"):
        list_path = single
        single = None

    if list_path:
        try:
            with open(list_path, "r") as f:
                for line in f:
                    clean = line.strip()
                    if clean and not clean.startswith("#"):
                        targets.append(clean if clean.startswith("http") else f"https://{clean}")
        except Exception as e:
            print(f"❌ Failed to load target list: {e}")
    elif single:
        targets.append(single if single.startswith("http") else f"https://{single}")
    else:
        print("⚠️ No targets defined.")

    return targets
