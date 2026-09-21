import os
import json
from hasher import hash_file

BASELINE_FILE = "baseline.json"

# Build baseline function
def build_baseline(paths):
    baseline = {}
    for path in paths:
        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                baseline[full_path] = hash_file(full_path)
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

# Check integrity function
def check_integrity(paths):
    from config import IGNORED_EXTENSIONS, IGNORED_FILES

    with open(BASELINE_FILE) as f:
        baseline = json.load(f)

    alerts = {
        "modified": [],
        "deleted": [],
        "new": []
    }

    current_files = {}

    for path in paths:
        for root, _, files in os.walk(path):
            for file in files:
                # --- Ignore rules start ---
                if any(file.endswith(ext) for ext in IGNORED_EXTENSIONS):
                    continue
                if file in IGNORED_FILES:
                    continue
                # --- Ignore rules end ---

                full_path = os.path.join(root, file)
                current_files[full_path] = hash_file(full_path)

    for file, old_hash in baseline.items():
        if file not in current_files:
            alerts["deleted"].append(file)
        elif current_files[file] != old_hash:
            alerts["modified"].append(file)

    for file in current_files:
        if file not in baseline:
            alerts["new"].append(file)

    return alerts
