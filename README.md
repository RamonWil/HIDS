## Host-Based Intrusion Detection System (HIDS)

A Python-based Host-Based Intrusion Detection System focused on **file integrity monitoring**. The system creates a SHA-256 baseline of monitored files and detects unauthorized or unexpected file changes by comparing the current system state against the stored baseline.

## Features

* Creates SHA-256 hashes for monitored files
* Builds and stores a trusted file integrity baseline
* Detects **modified files**
* Detects **deleted files**
* Detects **new files**
* Supports configurable monitored directories
* Supports file and extension ignore rules
* Displays security alerts in the terminal
* Logs detected activity for later review

## How It Works

The HIDS uses file hashing to identify changes within monitored directories.

1. **Baseline Creation**
   The system scans the configured directory and generates a SHA-256 hash for each file.

2. **Baseline Storage**
   File paths and their hashes are stored in `baseline.json`.

3. **Integrity Check**
   During later scans, the system generates new hashes and compares the current state against the original baseline.

4. **Change Detection**
   Files are classified as:

   * `MODIFIED` — the file exists, but its hash has changed
   * `DELETED` — the file existed in the baseline but is no longer present
   * `NEW` — the file was not present when the baseline was created

5. **Alerting & Logging**
   Detected changes are displayed in the terminal and written to the HIDS log.

## Project Structure

```text
host-based-intrusion-detection-system/
│
├── main.py             # Runs integrity checks and triggers alerts
├── file_monitor.py     # Builds baselines and compares file integrity
├── hasher.py           # Generates SHA-256 file hashes
├── alerts.py           # Displays security alerts
├── logger.py           # Records detected activity
├── config.py           # Monitoring and ignore configuration
├── baseline.json       # Stores trusted file hashes
└── hids_test/          # Test directory used for file monitoring
```

## Tech Stack

* **Python**
* **SHA-256**
* `hashlib`
* `os`
* `json`
* `logging`

The project uses Python's standard library and does not require third-party packages.

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/RamonWil/host-based-intrusion-detection-system.git
cd host-based-intrusion-detection-system
```

### 2. Configure the monitored directory

In `config.py`, specify the directory you want the HIDS to monitor:

```python
MONITORED_PATHS = [
    "./hids_test"
]
```

### 3. Create the initial baseline

On the first run, uncomment the following line in `main.py`:

```python
build_baseline(MONITORED_PATHS)
```

Then run:

```bash
python main.py
```

This generates `baseline.json`, containing the original SHA-256 hashes of the monitored files.

After creating the baseline, comment the line back out so the trusted baseline is not regenerated during each scan.

### 4. Test the HIDS

Modify, delete, or create a file inside the monitored directory.

Run:

```bash
python main.py
```

The HIDS will compare the current files against the stored baseline and generate alerts for detected changes.

Example:

```text
[ALERT] MODIFIED FILE: ./hids_test/notes.txt
[ALERT] DELETED FILE: ./hids_test/config/app.conf
[ALERT] NEW FILE: ./hids_test/config/new.conf
```

## Configuration

Monitoring behavior can be adjusted through `config.py`.

```python
MONITORED_PATHS = [
    "./hids_test"
]

ALLOWED_EXTENSIONS = [".conf", ".txt", ".sh"]

IGNORED_EXTENSIONS = [".log", ".tmp"]
IGNORED_FILES = ["baseline.json"]
```

The current integrity scanner uses the configured ignored files and extensions when performing integrity checks.

## Skills Demonstrated

This project provided hands-on experience with:

* Cybersecurity fundamentals
* File integrity monitoring
* Host-based intrusion detection concepts
* Cryptographic hashing
* Python system programming
* File system traversal
* Security logging and alerting
* Baseline-based change detection
* Modular software design

## Future Improvements

* Continuous file-system monitoring
* Apply configurable extension allowlisting during scans
* Email or desktop security notifications
* Severity levels for different alerts
* Improved event-specific logging
* Configurable detection rules
* Web-based monitoring dashboard

## Author

**[Ramon Williams](https://ramonwilliams.com)**
Computer Engineering — University of Kentucky

[Website](https://ramonwilliams.com) • [LinkedIn](https://www.linkedin.com/in/itsramon-williams)
