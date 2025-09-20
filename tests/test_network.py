from opsec_hardener import network, snapshots

def test_fake_eth_function_exists():
    # The real function is create_fake_eth
    assert hasattr(network, "create_fake_eth")

def test_snapshot_runs():
    result = snapshots.take_snapshot()
    # Ensure it produced a snapshot file path
    assert result.endswith(".txt")
