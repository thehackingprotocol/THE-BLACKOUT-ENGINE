import time
import shutil

def init_graphing(duration):
    print(f"📈 Live telemetry started. Duration: {duration}s\n")
    print("┌" + "─" * 58 + "┐")
    print("│{:^20}│{:^15}│{:^15}│".format("SECONDS", "SUCCESS", "FAILURES"))
    print("├" + "─" * 20 + "┼" + "─" * 15 + "┼" + "─" * 15 + "┤")

def update_graph(metrics):
    width = shutil.get_terminal_size((80, 20)).columns
    success = metrics["success"]
    fail = metrics["fail"]
    sent = metrics["sent"]
    if sent == 0: sent = 1  # prevent div-zero

    success_ratio = int((success / sent) * 30)
    fail_ratio = int((fail / sent) * 30)

    print("│{:^20}│{:^15}│{:^15}│".format(time.strftime("%H:%M:%S"), success, fail))
    print("│" + ("█" * success_ratio).ljust(30) + "│" + ("█" * fail_ratio).ljust(30) + "│")
    print("└" + "─" * 58 + "┘\n")
