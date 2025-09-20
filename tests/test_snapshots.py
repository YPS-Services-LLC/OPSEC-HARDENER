from src.opsec_hardener import snapshots

def test_snapshot_runs():
    snap = snapshots.take_snapshot()
    assert snap.endswith(".txt")
