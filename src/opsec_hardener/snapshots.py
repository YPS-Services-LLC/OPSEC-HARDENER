import os
import subprocess
from datetime import datetime

SNAPSHOT_DIR = os.path.expanduser("~/.opsec_snapshots")

def take_snapshot():
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    snap_file = os.path.join(SNAPSHOT_DIR, f"snapshot_{ts}.txt")

    with open(snap_file, "w") as f:
        f.write("=== SYSTEM SNAPSHOT ===\n")
        subprocess.run(["uname", "-a"], stdout=f)
        subprocess.run(["lsmod"], stdout=f)
        subprocess.run(["ss", "-tupn"], stdout=f)

    try:
        subprocess.run(["gpg", "--detach-sign", snap_file], check=False)
    except FileNotFoundError:
        pass

    return snap_file
