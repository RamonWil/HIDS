import logging

logging.basicConfig(
    filename="hids.log",
    level=logging.WARNING,
    format="%(asctime)s - %(message)s"
)

def log_alert(file):
    logging.warning(f"File modified: {file}")
