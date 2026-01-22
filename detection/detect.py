import json
from collections import defaultdict

THRESHOLD = 100
request_count = defaultdict(int)

with open("logs/access.log", "r") as file:
    for line in file:
        log = json.loads(line.strip())
        request_count[log["ip"]] += 1

print("\n=== ANALYSIS REPORT ===")
for ip, count in request_count.items():
    print(f"{ip} -> {count} requests")

print("\n=== ALERTS ===")
for ip, count in request_count.items():
    if count > THRESHOLD:
        print(f"[ALERT] Abnormal traffic from {ip}: {count} requests")
