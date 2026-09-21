from file_monitor import build_baseline, check_integrity
from config import MONITORED_PATHS
from logger import log_alert
from alerts import alert

# Uncomment only on first run
# build_baseline(MONITORED_PATHS)

alerts = check_integrity(MONITORED_PATHS)

for category, files in alerts.items():
    for file in files:
        msg = f"{category.upper()} FILE: {file}"
        log_alert(msg)
        alert(msg)
