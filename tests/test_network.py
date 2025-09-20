# tests/test_network.py
from opsec_hardener import network

def test_fake_eth_function_exists():
    assert hasattr(network, "fake_eth_interface")

# tests/test_snapshots.py
from opsec_hardener import snapshots

def test_snapshot_runs():
    result = snapshots.take_snapshot()
    assert "timestamp" in result
