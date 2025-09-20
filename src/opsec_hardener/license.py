import hashlib
import os
import sys

def check_file_integrity(file_path, expected_hash):
    if not os.path.exists(file_path):
        return False
    with open(file_path, "rb") as f:
        data = f.read()
        file_hash = hashlib.sha256(data).hexdigest()
    return file_hash == expected_hash

def enforce_integrity_or_exit(file_path, expected_hash):
    if not check_file_integrity(file_path, expected_hash):
        print("[!] Integrity check failed - shutting down.")
        sys.exit(1)
